class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k, n= 0, len(nums)
        for i in range(n):
            if nums[i] == val:
                nums[i] = 999
                k += 1
        nums.sort()
        return n-k
    

