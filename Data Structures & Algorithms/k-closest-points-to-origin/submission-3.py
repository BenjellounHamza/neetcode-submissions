class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            heapq.heappush(distances, (math.sqrt(point[0]**2 + point[1]**2), point))
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(distances)[1])
        return answer