class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]

        # pref[i] = 1 * .... * i - 1
        # suf[i] = i + 1 * ... * n
        # mult = suf[i] * pref[i]
        
        # [-1, 0, 1, 2, 3]
        # [1, -1, 0, 0, 0]
        # [0, 0, 6, 6, 3, 1]
        pref = [1]
        for i in range(1, len(nums)):
            pref.append(pref[-1] * nums[i - 1])
        suf = [1]
        for i in range(len(nums) - 2, -1, -1):
            suf = [suf[0] * nums[i + 1]] + suf
        answer = []
        for i in range(len(nums)):
            answer.append(pref[i] * suf[i])
        return answer
