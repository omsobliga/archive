def f(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]

    i = 0
    j = len(nums) - 1
    result = []
    while True:
        if i > j:
            break

        if nums[i] >= nums[j]:
            result.append(nums[i])
            i += 1
        else:
            result.append(nums[j])
            j -= 1
    return result[::-1]


print(f([-4, -3, 0, 1, 2, 5]))

