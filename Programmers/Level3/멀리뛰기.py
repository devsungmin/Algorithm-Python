# 피보나치 수열과 비슷한 문제 
# 점화식 = dp(n-1) + dp(n-2)
def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[0], dp[1] = 1, 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1234567
