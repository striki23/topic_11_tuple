# программа удаляет элемент из кортежа

line: tuple[str, ...] = ("P", "r", "o", "g", "r", "a", "m", "m", "i", "n", "g")
print(f'Исходный кортеж: {line}')
el: str = input('Укажите элемент для удаления: ')
if el not in line:
    print(f'"{el}" нет в кортеже')
else:
    while el in line:
        index_el: int = line.index(el)
        line_mod: tuple[str, ...] = line[:index_el] + line[index_el+1:]
        line = line_mod

    print(f'Измененный кортеж: {line_mod}')