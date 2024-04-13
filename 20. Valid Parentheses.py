class Solution:
    def isValid(self, s: str) -> bool:
        #for every letter in string
            #add on stack
            # if is other part of bracket, remove from stack
        string: list[str] = []
        len_string = 0
        for i in s:
            string.append(i)
            len_string+=1
            if (len_string>1):
                if ((string[-1] == '}' and string[-2] == '{') or 
                    (string[-1] == ']' and string[-2] == '[') or
                    (string[-1] == ')' and string[-2] == '(')):
                    string.pop()
                    string.pop()
                    len_string-=2
        if string == []:
            return True
        else:
            return False

if __name__ == '__main__':
    print(Solution().isValid('{(()[]){}}'))

