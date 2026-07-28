class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        if len(new_s) == 0:
            return True
        i, j = 0, len(new_s) - 1
        while new_s[i] == new_s[j] and i < j:
            i += 1
            j -= 1
        return i >= j