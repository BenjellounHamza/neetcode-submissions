class Solution:

    char_delimiter = ":"
    world_delimiter = "/"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty"
        answer = ""
        for j, s in enumerate(strs):
            for i , c in enumerate(s):
                answer += str(ord(c))
                if i < len(s) - 1:
                    answer += self.char_delimiter
            if j < len(strs) - 1:
                answer += self.world_delimiter
        print(answer)
        return answer


    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        answer = []
        for element in s.split("/"):
            maryam = ""
            for char in element.split(":"):
                if char == '':
                    maryam = ''
                    break
                maryam += chr(int(char))
            answer.append(maryam)
        print(answer)
        return answer

