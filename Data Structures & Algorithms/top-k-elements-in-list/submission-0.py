class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] = freq[n] + 1
            else:
                freq[n] = 1
        
        tas = []
        for element in freq:
            heapq.heappush(tas, (-freq[element], element))
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(tas)[1])
        
        return answer

