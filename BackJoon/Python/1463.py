import sys

num = int(sys.stdin.readline())

dp = [0 for _ in range(num+1)]

for i in range(2, num+1):
    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])

    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])

print(dp[-1])
