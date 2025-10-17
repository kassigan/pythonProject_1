# Task 1

import pandas as pd

# 1️⃣ Загружаем данные из CSV (укажи путь к своему файлу)
df = pd.read_csv("/Users/wanderlust/Downloads/earthquake_data_tsunami.csv")

# 2️⃣ Выводим первые 5 строк, чтобы посмотреть на структуру
print("Первые 5 строк данных:")
print(df.head())

# 3️⃣ Выводим общую информацию о данных
print("\nИнформация о данных:")
print(df.info())

# 4️⃣ Выводим статистическое описание (для числовых столбцов)
print("\nСтатистическое описание:")
print(df.describe())

# Task 2

# 1️⃣ Загружаем CSV-файл
file_path = "/Users/wanderlust/Downloads/dz.csv"
df = pd.read_csv(file_path)

# 2️⃣ Проверим, как выглядят данные
print("Первые 5 строк:")
print(df.head(), "\n")

# 3️⃣ Проверим информацию о типах данных
print("Информация о данных:")
print(df.info(), "\n")

# 4️⃣ Группируем по городу и считаем среднюю зарплату
avg_salary_by_city = df.groupby('City')['Salary'].mean()

# 5️⃣ Выводим результат
print("Средняя зарплата по городам:")
print(avg_salary_by_city)

