# Базовая обработка Исключений
"""""
def save_divide(a,b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("None")


save_divide(20,0)
save_divide(20,5)
"""""
"""""
#обработка множества исключений

while True:
    try:
        # Запрашиваем у пользователя число
        customer_number = input("Введите число: ")

        # Преобразуем введенное значение в целое число
        number = int(customer_number)

        # Выводим результат
        print(f"Вы ввели число: {number}")

        # Выход из цикла, если преобразование успешно
        break
    except ValueError:
        # Если возникла ошибка, выводим сообщение и просим ввести число снова
        print("Невозможно преобразовать введенное значение в целое число.")
        print("Пожалуйста, введите число еще раз.")
"""""


# Обработка исключений прошлых программ
while True:
    print('Please enter 2 numbers, end and start of the range to find out, \
how many even numbers are in it')

    try:
        first_num = int(input('Enter first number: '))
        second_num = int(input('Enter end number: '))

    # variable to store even numbers
        even_count = 0
        even_list = []

    # Loop to find even numbers
        for i in range(first_num, second_num):
            if i % 2 == 0: # Check if the number is even
                even_count += 1
                even_list.append(i)
         # Output the result
            print("Even numbers in the range:", even_list, "Total even numbers:", even_count)
        break
    except ValueError:
        print(f"It's not a number")




