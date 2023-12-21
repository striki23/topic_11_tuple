# программа заменяет последнее значение кортежей в списке

nums: list[tuple, ...] = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(f'Исходный список кортежей: {nums}')
el: int = int(input('Укажите значение: '))
# заменяем последний элемент списка
nums[-1] = nums[-1][:len(nums[-1])-1] + (el,)
print(f'Измененный список кортежей: {nums}')
