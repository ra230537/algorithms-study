class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_table = {}
        for i in range(len(nums)):
            if not nums[i] in hash_table.keys():
                hash_table[nums[i]] = []
            hash_table[nums[i]].append(i)
        print(hash_table)
        for value in nums:
            if (hash_table.get(target-value, None) != None):
                if (target == value * 2 and len(hash_table[value]) > 1) or (target != value * 2):
                    a = hash_table[value][-1]
                    hash_table[value].pop()
                    b = hash_table[target - value][-1]
                    return [a, b]
    


if __name__ == '__main__':
    print(Solution().twoSum([3, 4, 2],6))