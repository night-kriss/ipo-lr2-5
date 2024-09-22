number = int(input("Введите 8-значное число: "))
if 10000000 <= number <= 99999999:
    result = sum(int(digit) for digit in str(number))
    print("Сумма цифр числа:", result)
else:
    print("Пожалуйста, введите корректное 8-значное число.")
