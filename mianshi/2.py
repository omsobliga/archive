def f(nums):
    if len(nums) == 1:
        return True

    max_pos = 0
    for i, n in enumerate(nums):
        max_pos = max(max_pos, i + n)
        if max_pos <= i and i != len(nums) - 1:
            return False
    return True


print(f([2, 0, 0]))
print(f([0]))
print(f([2, 3, 1, 1, 4]))
print(f([3, 2, 1, 0, 4]))
