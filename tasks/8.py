# программа ищет повторяющиеся элементы кортежа

nums: tuple[int, ...] = (2, 4, 5, 6, 2, 3, 4, 4, 7)
print(f'Исходный кортеж: {nums}')
el: int = int(input('Укажите искомый элемент: '))
if el not in nums:
    print(f'"{el}" нет в кортеже')
else:
    print(nums.count(el))
