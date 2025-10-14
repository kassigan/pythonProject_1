from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


class WikipediaBrowser:
    def __init__(self):
        # Настройка драйвера
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Раскомментируйте, если не хотите видеть браузер
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.current_paragraph_index = 0
        self.current_page_title = ""

    def search_wikipedia(self, query):
        """Выполняет поиск по запросу и переходит на первую статью"""
        try:
            self.driver.get("https://ru.wikipedia.org/wiki/Заглавная_страница")

            # Поисковая строка
            search_box = self.wait.until(
                EC.presence_of_element_located((By.ID, "searchInput"))
            )
            search_box.clear()
            search_box.send_keys(query)

            # Кнопка поиска
            search_button = self.driver.find_element(By.ID, "searchButton")
            search_button.click()

            # Ждем загрузки результатов
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".mw-page-title-main"))
            )

            self.current_page_title = self.driver.find_element(By.CSS_SELECTOR, ".mw-page-title-main").text
            self.current_paragraph_index = 0
            print(f"\nПерешли на статью: {self.current_page_title}")
            return True

        except Exception as e:
            print(f"Ошибка при поиске: {e}")
            return False

    def get_paragraphs(self):
        """Получает все параграфы текущей статьи"""
        try:
            paragraphs = self.driver.find_elements(By.CSS_SELECTOR, "div.mw-parser-output > p")
            return [p for p in paragraphs if p.text.strip()]
        except Exception as e:
            print(f"Ошибка при получении параграфов: {e}")
            return []

    def show_next_paragraph(self):
        """Показывает следующий параграф статьи"""
        paragraphs = self.get_paragraphs()

        if not paragraphs:
            print("В статье нет параграфов для отображения.")
            return False

        if self.current_paragraph_index < len(paragraphs):
            paragraph = paragraphs[self.current_paragraph_index]
            print(f"\n--- Параграф {self.current_paragraph_index + 1} ---")
            print(paragraph.text)
            self.current_paragraph_index += 1
            return True
        else:
            print("Вы достигли конца статьи.")
            return False

    def get_related_links(self):
        """Получает список связанных страниц из статьи"""
        try:
            # Ищем ссылки в основном содержании статьи
            content_div = self.driver.find_element(By.ID, "mw-content-text")
            links = content_div.find_elements(By.CSS_SELECTOR, "a[href^='/wiki/']")

            related_links = []
            for link in links[:10]:  # Берем первые 10 ссылок
                href = link.get_attribute("href")
                text = link.text.strip()
                if text and ":" not in href and "#" not in href and text not in related_links:
                    related_links.append((text, href))
                    if len(related_links) >= 5:  # Ограничиваем 5 ссылками
                        break

            return related_links
        except Exception as e:
            print(f"Ошибка при получении связанных ссылок: {e}")
            return []

    def navigate_to_link(self, link_url):
        """Переходит по указанной ссылке"""
        try:
            self.driver.get(link_url)

            # Ждем загрузки заголовка
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".mw-page-title-main, h1"))
            )

            # Получаем заголовок страницы
            try:
                title_element = self.driver.find_element(By.CSS_SELECTOR, ".mw-page-title-main")
            except:
                title_element = self.driver.find_element(By.CSS_SELECTOR, "h1")

            self.current_page_title = title_element.text
            self.current_paragraph_index = 0

            print(f"\nПерешли на статью: {self.current_page_title}")
            return True

        except Exception as e:
            print(f"Ошибка при переходе по ссылке: {e}")
            return False

    def show_menu(self):
        """Показывает меню действий"""
        print(f"\n=== Текущая статья: {self.current_page_title} ===")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("\nВыберите действие (1-3): ").strip()
        return choice

    def show_related_links_menu(self):
        """Показывает меню связанных страниц"""
        links = self.get_related_links()

        if not links:
            print("Не найдено связанных страниц.")
            return None

        print("\n=== Связанные страницы ===")
        for i, (title, url) in enumerate(links, 1):
            print(f"{i}. {title}")
        print(f"{len(links) + 1}. Вернуться назад")

        try:
            choice = int(input(f"\nВыберите страницу (1-{len(links) + 1}): ").strip())
            if 1 <= choice <= len(links):
                return links[choice - 1][1]  # Возвращаем URL
            elif choice == len(links) + 1:
                return "back"
            else:
                print("Неверный выбор.")
                return None
        except ValueError:
            print("Пожалуйста, введите число.")
            return None

    def run(self):
        """Основной цикл программы"""
        print("=== Википедия Браузер ===")

        # Шаг 1: Запрос первоначального поиска
        initial_query = input("Введите поисковый запрос: ").strip()
        if not initial_query:
            print("Запрос не может быть пустым.")
            return

        if not self.search_wikipedia(initial_query):
            print("Не удалось выполнить поиск. Завершение программы.")
            return

        # Основной цикл навигации
        while True:
            choice = self.show_menu()

            if choice == "1":
                # Листать параграфы
                if not self.show_next_paragraph():
                    print("Больше нет параграфов для отображения.")

            elif choice == "2":
                # Перейти на связанную страницу
                while True:
                    link_url = self.show_related_links_menu()

                    if link_url == "back":
                        break
                    elif link_url:
                        if self.navigate_to_link(link_url):
                            # После перехода показываем подменю для новой статьи
                            sub_choice = input(
                                "\n1. Листать параграфы этой статьи\n2. Вернуться к выбору связанных страниц\nВыберите действие (1-2): ").strip()

                            if sub_choice == "1":
                                self.show_next_paragraph()
                                # После просмотра параграфа возвращаемся к выбору связанных страниц
                                continue
                            elif sub_choice == "2":
                                continue
                            else:
                                print("Неверный выбор, возвращаемся к меню.")
                                break
                        else:
                            print("Не удалось перейти по ссылке.")
                    else:
                        break

            elif choice == "3":
                # Выход
                print("Выход из программы...")
                break

            else:
                print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

    def close(self):
        """Закрывает браузер"""
        self.driver.quit()


def main():
    browser = WikipediaBrowser()
    try:
        browser.run()
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        browser.close()


if __name__ == "__main__":
    main()