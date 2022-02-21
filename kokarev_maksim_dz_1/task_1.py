"""
1.	Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
a.	до минуты: <s> сек;
b.	до часа: <m> мин <s> сек;
c.	до суток: <h> час <m> мин <s> сек;
d.	* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:
duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек
подумайте, можно ли использовать цикл для проверки работы кода сразу для нескольких значений продолжительности,
будет ли тут полезен список?
"""
# Ввод числа и проверка
while True:
    duration = input('Input duration in seconds =')
    if duration.isdigit():
        duration = int(duration)
        break
    else:
        print('Вы ввели не число, пожалуйста введите корректно')
        continue
attributes = {0: 'сек', 1: 'мин', 2: 'час', 3: 'дн'}
numbers = []

# Вычисление на какие отрезки разбить время
if duration < 60:
    count = 0
    numbers.append(duration)
elif 60 <= duration < 3600:
    count = 1
    minutes = duration // 60
    seconds = duration % 60
    numbers = [seconds, minutes]
elif 3600 <= duration < 86400:
    count = 2
    hours = duration // 60 // 60
    minutes = duration // (hours * 60) % 60
    seconds = (duration % 60) % 60
    numbers = [seconds, minutes, hours]
else:
    count = 3
    days = duration // 60 // 60 // 24
    _duration = duration - days * 60 * 60 * 24
    if _duration < 60:
        numbers = [_duration, 0, 0, days]
    elif 60 <= _duration < 3600:
        minutes = _duration // 60
        seconds = _duration % 60
        numbers = [seconds, minutes, 0, days]
    else:
        hours = _duration // 60 // 60
        minutes = _duration // (hours * 60) % 60
        seconds = (_duration % 60) % 60
        numbers = [seconds, minutes, hours, days]
result = []

# Запись в текстовом виде и сопоставление буквенных символов и цифр
for i in range(count + 1):
    # Проверка, чтоб не выводить нулевые значения
    if numbers[i] == 0:
        continue
    else:
        result.append(f'{numbers[i]} {attributes[i]}')
result.reverse()
result_string = ' '.join(result)
print(f'При переводе введенная длительность получается = {result_string}')
