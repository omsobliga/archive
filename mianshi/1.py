import sys


def _f(nums):
    min_value = sys.maxsize
    result = 0
    for i, n in enumerate(nums):
        if n < min_value:
            min_value = n
            for m in nums[i+1:]:
                result = max(result, m - n)
        else:
            continue
    return result


def f(nums):
    min_value = nums[0]
    max_value = nums[0]
    result = 0
    for n in nums:
        if n < min_value:
            min_value = n
            max_value = n

        if n > max_value:
            max_value = n
            result = max(result, max_value-min_value)
    return result


print(f([1, 2, 3, 4]))
print(f([4, 3, 2, 1]))
print(f([1, 2, 1]))
print(f([1, 2, 1, 4]))


