class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       
        k = 0
        free_pos = -1

        for i, n in enumerate(nums):
            if n == val:
                for j in range(i+1, len(nums)):
                    if nums[j] != val:
                        nums[i], nums[j] = nums[j], nums[i]
            else:
                k=0
        for n in nums[::-1]:
            if n == val:
                k+=1
                continue
            break
        print(nums)
        return len(nums)-k
        