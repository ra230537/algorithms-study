
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Find k
        i = 0
        k = len(nums)
        j = len(nums) - 1
        while i < j:
            while nums[i] != val and i < j:
                i += 1
            while nums[j] == val and i < j:
                j -= 1
                # k+=1
            if i < j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                k-=1
        print(nums)
        print(k)
        return k
    
if __name__ == '__main__':
    Solution().removeElement(nums=[0,1,2,2,3,0,4,2], val=2)