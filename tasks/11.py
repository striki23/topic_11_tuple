# программа преобразует заданную строку в кортеж (пробелы убираются)
line: str = input('Введите ваш текст: ')
print('Тип:', type(line))
line_mod: tuple[str, ...] = tuple(''.join(line.split()))
print('Строка преобразованная в кортеж:', line_mod)

# Python 3.9 is cool!