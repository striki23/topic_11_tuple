# программа преобразовывает кортеж в строку

line_tpl: tuple[str, ...] = (
    "P", "r", "o", "g", "r", "a", "m", "m", "i", "n", "g"
)
line_str: str = ''.join(line_tpl)
print('Исходный кортеж:', line_tpl, '\nСтрока:', line_str)
