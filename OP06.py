"""
# Задание 2. Создание модуля с функциями арифметики
import arithmetic
print (arithmetic.substraction(15,9))
print (arithmetic.addition(4,10))
print (arithmetic.multiplication(32,2))
print (arithmetic.division(45, 5))
"""
"""""
# Задание 3. Случайный выбор элемента

import random

name_list = [ "Mailo ", "Michael ", "Jakob ", "Thomas ", "Linus ", "Lukas ", "Jonas ", "Paul  ", "Lina ", "Emilia ", "Emma ", "Lea ", "Laura ", "Ella ", "Lia ", "Anna "]

result = random.sample(name_list, 5)
print (result)
"""""

# Задание 1. Создание и запись в файл

user_text = input("please enter your text here ")

file = open("user_data.txt", "a", encoding="utf-8")
file.write(user_text + "\n")

print ("Content of file")
file = open("user_data.txt", "r")
print (file.read())

file.close ()