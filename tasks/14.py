# Программа выводит кортеж из введенной строки с учетом заданного шага
line: tuple[str, ...] = tuple(input('Введите ваш текст: ').split())
step: int = int(input('Укажите шаг, положительное целое число: '))
print('Исходный кортеж:', line)
print('Измененный кортеж:', line[::step])

# Например, в новый кортеж включаются элементы, отстоящие друг от друга на 3 позиции