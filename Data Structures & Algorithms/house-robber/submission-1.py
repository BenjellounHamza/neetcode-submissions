class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        answer = []
        def helper(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(nums[i] + helper(i + 2), helper(i + 1))
            return dp[i]
        
        return helper(0)

        