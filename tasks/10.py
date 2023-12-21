# программа удаляет пустые кортежи из списка кортежей

lst: list[tuple, ...] = [
    (), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)
]
while () in lst:
    lst.remove(())
print(lst)

