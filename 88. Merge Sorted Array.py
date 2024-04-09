class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        final_list = []
        new_num1 = nums1[:m]
        while i < m and j < n:
            if (new_num1[i] < nums2[j]):
                final_list.append(new_num1[i])
                i+=1
            else:
                final_list.append(nums2[j])
                j+=1
        if i>=m:
            for final_j in range(j, n):
                final_list.append(nums2[final_j])
        if j>=n:
            for final_i in range(i, m):
                final_list.append(new_num1[final_i])
        for index in range(len(final_list)):
            nums1[index] = final_list[index]
        return nums1

if __name__ == '__main__':
    solucao = Solution()
    print(solucao.merge(nums1 = [2, 0], m = 1, nums2 = [1], n = 1))