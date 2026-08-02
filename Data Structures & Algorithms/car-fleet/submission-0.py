class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        def time(s, pos):
            return (target - pos) / s

        array = []

        for pos, s in zip(position, speed):
            array.append((pos, s))

        array = sorted(array, key=lambda x: x[0], reverse=True)
        stack = []
        for element in array:
            pos, s = element
            if len(stack) > 0 and time(s, pos) <= stack[-1]:
                continue
            else:
                stack.append(time(s, pos))
        
        return len(stack)
            


            



        
            

