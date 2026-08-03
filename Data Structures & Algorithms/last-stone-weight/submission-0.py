class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = []
        for s in stones:
            heapq.heappush(l, -s)
        
        while len(l) > 1:
            left = heapq.heappop(l)
            right = heapq.heappop(l)
            if left == right:
                continue
            elif left > right:
                heapq.heappush(l, right - left)
            else:
                heapq.heappush(l, left - right)
        if len(l) == 1:
            return -l[0]
        else:
            return 0