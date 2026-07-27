class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for s in strs:
            code = self.encode(s)
            if code in answer:
                answer[code].append(s)
            else:
                answer[code] = [s]
        
        return [v for v in answer.values()]

    def encode(self, s):
        code = [0 for _ in range(ord("a"), ord("z") + 1)]
        for c in s:
            code[ord(c) - ord("a")] += 1
        return str(code)
        
