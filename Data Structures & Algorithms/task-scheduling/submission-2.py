class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = []
        count = {}
        for task in tasks:
            if task in count:
                count[task] += 1
            else:
                count[task] = 1
            
        for task in count.keys():
            heapq.heappush(l, (-count[task]))
        current_time = 0
        cooldown_queue = deque()
        while len(l) != 0 or len(cooldown_queue) != 0:
            print(l)
            print(cooldown_queue)
            print(current_time)
            if len(l) > 0:
                number = heapq.heappop(l)
                if -number > 1:
                    cooldown_queue.append((current_time + n, number + 1))
            if len(cooldown_queue) > 0 and cooldown_queue[0][0] <= current_time:
                heapq.heappush(l, cooldown_queue.popleft()[1])
            current_time += 1
        return current_time
                