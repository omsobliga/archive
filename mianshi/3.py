import random


def f(m, n):
    m = m * 100
    result = []
    for i in range(n):
        if i == n - 1:
            result.append(m)
            break

        max_price = m - (n - i - 1)
        price = random.randint(1, max_price)
        result.append(price)
        m = m - price
    return result, sum(result)


print(f(100, 5))
print(f(10, 10))
print(f(10, 20))
