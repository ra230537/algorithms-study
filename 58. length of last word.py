class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        valid_word = False
        for i in range(len(s) -1, -1, -1):
            if s[i] != ' ':
                valid_word = True
            if (s[i]!= ' ' and valid_word):
                count += 1
            if valid_word and s[i] == ' ':
                return count
        return count