class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        answer = 100*100
        dp = [100*100 for _ in range(len(cost) + 1)]
        def helper(cost, i, tmp):
            nonlocal answer
            if i >= len(cost):
                answer = min(tmp, answer)
                return
            if tmp >= dp[i]:
                return
            dp[i] = min(tmp, dp[i])

            helper(cost, i + 1, tmp + cost[i])
            helper(cost, i + 2, tmp + cost[i])
        helper([0] + cost, 0, 0)
        return answer
        