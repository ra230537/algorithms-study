class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create a hash to count the letters occurrences
        hash_table = {}
        for letter in magazine:
            if not letter in hash_table.keys():
                hash_table[letter] = 0
            hash_table[letter]+=1
        for letter in ransomNote:
            if not letter in hash_table.keys() or hash_table[letter] == 0:
                return False
            hash_table[letter] -= 1
        return True

if __name__ == '__main__':
    print(Solution().canConstruct('aada','aaabc'))