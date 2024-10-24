def f(n):
    dp = [[]] * n
    for i in range(n):
        dp[i] = [-1] * n

    for k in range(0, n):
        for i in range(0, n):
            j = i + k
            if j >= n:
                break
            if k == 0:
                dp[i][j] = 1
            else:
                for p in range(i, j):
                    dp[i][j] = max(dp[i][j], dp[i][p] * dp[p+1][j])
                    if k != n-1:
                        dp[i][j] = max(dp[i][j], k + 1)
                    # print(k, i, j, p, dp[i][j])
    return dp[0][n-1]


print(f(1))
print(f(2))
print(f(10))

