def f(nums):
    i = 0
    j = len(nums) - 1
    total = 0
    while True:
        if i > j:
            break
        if nums[i] > nums[j]:
            j -= 1
            total += 1
        elif nums[i] < nums[j]:
            i += 1
            total += 1
        else:
            if i == j:
                total += 1
            i += 1
            j -= 1
    return total


# print(f([1, 2, 3, 2, 1]))
print(f([1, 2, 5, 4, 3]))
