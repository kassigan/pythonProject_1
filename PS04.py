# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
# листать параграфы текущей статьи;
# перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
# - перейти на одну из внутренних статей.
# выйти из программы.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


def open_wikipedia():
    """Создаём и настраиваем браузер"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # открыть в полном окне
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return browser


def search_article(browser, query):
    """Поиск статьи на Википедии"""
    browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)


def read_article(browser):
    """Листание параграфов и переходы по ссылкам"""
    while True:
        paragraphs = browser.find_elements(By.CSS_SELECTOR, "p")
        print("\n--- Текущие параграфы статьи ---")
        for i, p in enumerate(paragraphs[:5], start=1):
            print(f"{i}. {p.text[:150]}...")  # первые 150 символов

        print("\nВыберите действие:")
        print("1 — перейти к следующему набору параграфов")
        print("2 — перейти на одну из связанных страниц")
        print("3 — выйти из программы")

        choice = input("Ваш выбор: ")

        if choice == "1":
            browser.execute_script("window.scrollBy(0, window.innerHeight);")
            time.sleep(2)

        elif choice == "2":
            links = browser.find_elements(By.CSS_SELECTOR, "#bodyContent a[href^='/wiki/']")
            unique_links = []
            for link in links:
                href = link.get_attribute("href")
                if href not in unique_links and ":" not in href:  # отсекаем служебные страницы
                    unique_links.append(href)
            if not unique_links:
                print("Связанных страниц не найдено.")
                continue

            print("\nСвязанные страницы:")
            for i, link in enumerate(unique_links[:10], start=1):
                print(f"{i}. {link}")

            num = input("Введите номер ссылки для перехода: ")
            if num.isdigit() and 1 <= int(num) <= len(unique_links[:10]):
                browser.get(unique_links[int(num) - 1])
                time.sleep(2)
            else:
                print("Неверный выбор. Возврат к текущей статье.")

        elif choice == "3":
            print("Выход из программы...")
            break
        else:
            print("Неверный ввод.")


def main():
    browser = open_wikipedia()
    print("🔎 Добро пожаловать в Википедию (через Selenium)!")
    try:
        query = input("Введите запрос: ")
        search_article(browser, query)
        read_article(browser)
    finally:
        browser.quit()


if __name__ == "__main__":
    main()
