class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_element = set(nums)
        answer = 0
        for num in nums:
            if num - 1 not in set_element:
                # means that the num is the begning of the serie
                i = num + 1
                while i > num and i in set_element:
                    i += 1
                answer = max(answer, i - num)
        return answer
                
                    

