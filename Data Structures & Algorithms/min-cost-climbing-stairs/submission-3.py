class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        answer = 100*100
        dp = [-1 for _ in range(len(cost) + 1)]
        def helper(i):
            if i >= len(cost):
                return 0
            if dp[i] != -1:
                return dp[i] 
            dp[i] = min(helper(i + 1), helper(i + 2)) + cost[i]
            return dp[i]
        return min(helper(0), helper(1))
        