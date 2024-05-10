# Using Dynamic Programming
from typing import List

def minSubsetSumDifference(arr: List[int], n: int) -> int:
    # Calculate total sum and initialize DP table
    total_sum = sum(arr)
    dp = [[False]*(total_sum + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = True
    if arr[0] <= total_sum:
        dp[0][arr[0]] = True

    # Dynamic programming
    for i in range(1, n):
        for target in range(1, total_sum + 1):
            not_taken = dp[i-1][target]
            taken = False
            if arr[i] <= target:
                taken = dp[i-1][target - arr[i]]
            dp[i][target] = not_taken or taken

    # Find the minimum difference
    mini = float('inf')
    for i in range(total_sum + 1):
        if dp[n-1][i]:
            diff = abs(total_sum - 2 * i)
            mini = min(mini, diff)
    return mini
