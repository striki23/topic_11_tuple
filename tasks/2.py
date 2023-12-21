# програма  переворачивает кортеж (5, 7, 9, 12)

nums: tuple[int, ...] = (5, 7, 9, 12)
nums_rev: tuple[int, ...] = tuple(reversed(nums))

# var 2
# nums_rev = nums[::-1]

print(nums_rev)
