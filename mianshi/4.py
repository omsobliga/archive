def merge(a, m, b, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while True:
        if i < 0 and j < 0:
            break

        if j < 0 or (i >= 0 and j >= 0 and a[i] > b[j]):
            a[k] = a[i]
            k -= 1
            i -= 1
        elif (i >= 0 and j >= 0 and a[i] == b[j]):
            a[k] = a[i]
            a[k-1] = b[j]
            k -= 2
            i -= 1
            j -= 1
        elif i < 0 or (i >= 0 and j >= 0 and a[i] < b[j]):
            a[k] = b[j]
            k -= 1
            j -= 1
    return a


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

