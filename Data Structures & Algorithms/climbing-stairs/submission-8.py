class Solution:

    def climbStairs(self, n: int) -> int:

        results = {1: 1}

        def helper(n):
            if n in results:
                return results[n]
            if n <= 0:
                return 1
            left = helper(n - 1)
            right = helper(n - 2)
            results[n] = left + right
            return left + right
        return helper(n)