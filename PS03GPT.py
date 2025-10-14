import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")


def word_game():
    print("Добро пожаловать в игру")
    translator = GoogleTranslator()  # ← добавляем сюда, чтобы можно было вызывать translate()

    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # 🔹 1. Переводим определение перед показом
        definition_ru = GoogleTranslator(source='en', target='ru').translate(word_definition)

        print(f"Значение слова - {word_definition}")
        print(f"(Перевод: {definition_ru})")  # ← добавили перевод определения

        user = input("Что это за слово? ")

        if user == word:
            print("Все верно!")
        else:
            # 🔹 2. Переводим слово при показе правильного ответа
            word_ru = GoogleTranslator(source='en', target='ru').translate(word)
            print(f"Ответ неверный, было загадано это слово - {word} ({word_ru})")

        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()
