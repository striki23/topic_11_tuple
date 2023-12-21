# программа преобразовывает кортеж строковых значений
# в кортеж целочисленных значений

tpl_tpl: tuple[tuple, ...] = (('363', '13'), ('1616', '55'), ('468', '10'))
print('Исходные значения кортежа:', tpl_tpl)
new_tpl: tuple[tuple, ...] = tuple(tuple(int(i) for i in tpl) for tpl in tpl_tpl)
print('Новые значения кортежа:', new_tpl)

# -------var 2--------
# print('Исходные значения кортежа:', tpl_tpl)
# # преобразовываем кортеж из кортежей в список списков
# lst_lst: list[list, ...] = [list(i) for i in tpl_tpl]
# # создаем новый список c подсписками, элементы которых
# # преобразуем в int
# new_lst: list[list, ...] = []
# for i in lst_lst:
#     el: list[int, ...] = [int(num) for num in i]
#     # перед сохранением подсписка с числами
#     # переводим его обратно в tuple
#     new_lst.append(tuple(el))
# print('Новые значения кортежа:', tuple(new_lst))