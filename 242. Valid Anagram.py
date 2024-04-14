class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        if len(s)!=len(t):
            return False
        for letter_s in s:
            if letter_s in dict_s:
                dict_s[letter_s]+=1
            else:
                dict_s[letter_s] = 1
        for letter_t in t:
            if dict_s.get(letter_t, None) == None:
                return False
            else:
                dict_s[letter_t]-=1
            if dict_s[letter_t] < 0:
                return False
        return True
    
if __name__ == '__main__':
    print(Solution().isAnagram(s = "anagram", t = "nagaram"))