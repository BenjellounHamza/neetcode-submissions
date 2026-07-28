class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # surface = min(hight) * distance
        surface = 0
        i, j = 0, len(heights) - 1
        while i < j:
            surface = max(surface, min(heights[i], heights[j])* (j - i))
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return surface 