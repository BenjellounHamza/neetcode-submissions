class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        answer = []

        mapping = {}

        def subsets(nums, index):
            if len(nums) == index:
                return [[]]
            ans = []
            temp = subsets(nums, index + 1)
            for t in temp:
                ans.append(t)
                t_copy = list(t)
                t_copy.append(nums[index])
                ans.append(t_copy)
            return ans
        
        return subsets(nums, 0)