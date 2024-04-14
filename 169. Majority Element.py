class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums = sorted(nums)
        count = 0
        max_count = -1
        majority_value = nums[0]
        for i,_ in enumerate(nums):
            if (i > 0):
                if (nums[i] == nums[i-1]):
                    count += 1
                else:
                    count = 1
            else:
                count += 1 
            if count > max_count:
                max_count = count
                majority_value = nums[i]
        return majority_value
    
if __name__ == '__main__':
    Solution().majorityElement(nums=[6,6,6,7,7])