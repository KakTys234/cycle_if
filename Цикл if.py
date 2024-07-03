# x = int(input('введите число: '))
# x = int(x)
#
# if x > 0:
#     y = 2*x
#     print('Значение функции Y: 'y)
# else:
#     print('Значение неверно')

# x = int(input('введите число: '))
# x = int(x)
#
# if x <= 0:
#     y = x**2
#     print('Значение функции Y: 'y)
# else:
#     print('Значение неверно')

# x = int(input('введите число: '))
# x = int(x)
#
# if x > 5:
#     y = x - 1
#     print('Значение функции Y: ', y)
# else:
#     print('Значение неверно')


# x = int(input('введите число: '))
# x = int(x)
#
# if 5 <= x <= 5:
#     y = x**2 + x
#     print('Значение функции Y: ', y)
# else:
#     print('Значение неверно')

# x = int(input('введите число: '))
# x = int(x)
#
# if x < -5:
#     y = x**2
#     print('Значение функции Y: ', y)
# else:
#     print('Значение неверно')

# number = [345, 128, 581]
# if number[0] > number[1] and number[0] > number[2]:
#     print(number[0])
# elif number[1] > number[0] and number[1] > number[2]:
#     print(number[1])
# else:
#     print(number[2])

# num = int(input('введите число: '))
# if num % 2 == 0:
#     print(num, 'Четное число')
# else:
#     print()

# num = int(input('введите число: '))
# if num > 0:
#     print(num, 'Число положительное')
# elif num < 0:
#     print(num, 'Число отрицательное')
# else:
#     print(num)

# a = int(input('Первый катет равен '))
# b = int(input('Второй кактет равен '))
# c = int(input('Гипотенуза равна '))
# if a == b == c:
#     print('Треугольник abc - равносторонний')
# elif b == a < c or b == a > c:
#     print('Треугольник abc - равнобедренний')
# else:
#     print('Треугольник abc - разносторонний')

# winter = ['декабрь', 'январь', 'февраль']
# spring = ['март', 'апрель', 'май']
# summer = ['июнь', 'июль', 'август']
# autumn = ['сентябрь', 'октябрь', 'ноябрь']
# season = input('Какой сегодня месяц? ')
# if season in winter:
#     print('На дворе зима!')
# elif season in spring:
#     print('На дворе весна')
# elif season in summer:
#     print('На дворе лето')
# else:
#     print('На дворе осень')

num = int(input('введите число: '))
if num == 1:
    print(num, 'Не является простым или составным числом')
elif num == 0:
    print(num)
elif (num > 2 and num != 3) and (num % 2 == 0 or num % 3 == 0):
    print(num, ' - это составное число')
else:
    print(num, ' - это простое число')
