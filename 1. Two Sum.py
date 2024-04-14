class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], index]
            num_map[num] = index


if __name__ == '__main__':
    print(Solution().twoSum([3, 4, 2],6))