class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        indexof = -1
        for i, element in enumerate(self.nums):
            if val > element:
                indexof = i
                break
        if indexof == -1:
            self.nums.append(val)
        else:
            self.nums = self.nums[:indexof] + [val] + self.nums[indexof:]
        return self.nums[self.k - 1]
        
