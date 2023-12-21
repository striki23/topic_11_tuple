# программа преобразовывает список в кортеж

nums_lst: list[int, ...] = [5, 10, 7, 4, 15, 3]
nums_tpl: tuple[int, ...] = tuple(nums_lst)
print('Исходный список:', nums_lst, '\nКортеж:', nums_tpl)
