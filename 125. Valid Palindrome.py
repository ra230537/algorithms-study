class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        set_values = set('abcdefghijklmnopqrstuvwxyz0123456789')
        i = 0
        j = len(s)-1
        while i < j:
            while s[i] not in set_values and i < j:
                i+=1
            while s[j] not in set_values and i < j:
                j-=1
            if (i < j):
                if (s[i] != s[j]):
                    return False
            i+=1
            j-=1
        return True


            
if __name__=='__main__':
    asw = Solution().isPalindrome('A man, a plan, a canal: Panama')
    print(asw)