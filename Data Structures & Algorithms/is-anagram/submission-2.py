class Solution:

    def freq(self, s):
        d = {}
        for element in s:
            if element in d:
                d[element] = d[element] + 1
            else:
                d[element] = 1
        return d 

    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = self.freq(s)
        freq_t = self.freq(t)
        for k in freq_s.keys():
            if k not in freq_t:
                return False
            elif freq_t[k] != freq_s[k]:
                return False
        return len(freq_t) == len(freq_s)
