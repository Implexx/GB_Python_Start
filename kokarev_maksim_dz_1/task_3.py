"""
3.	Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
"""

# приводим к числу введенное значение процентов
number = int(input('введите число процентов от 0 до 100 = '))

# если число входит в заданный промежуток от 0 до 100
if 101 > number >= 0:
    # числа 11, 12, 13, 14 исключения из общего правила, поэтому вынесены в отдельное условие
    if number in (12, 11, 13, 14):
        print(f'Вы ввели {number} процентов')
    else:
        remainder = number % 10
        if remainder == 1:
            print(f'Вы ввели {number} процент')
        elif remainder == 2 or remainder == 3 or remainder == 4:
            print(f'Вы ввели {number} процента')
        elif remainder > 4 or remainder == 0:
            print(f'Вы ввели {number} процентов')

else:
    print(f'Вы ввели число, не удовлетворяющее условию задачи')

print('------------------'*5)

print('Для проверки вывод всех вариантов от 0 до 100:')
for number in range(101):
    if number in (11, 12, 13, 14):
        print(f'{number} процентов')
    else:
        remainder = number % 10
        if remainder == 1:
            print(f'{number} процент')
        elif remainder == 2 or remainder == 3 or remainder == 4:
            print(f'{number} процента')
        elif remainder > 4 or remainder == 0:
            print(f'{number} процентов')