class Solution:
    def canJump(self, nums: List[int]) -> bool:

        farthest = 0

        for i, n in enumerate(nums):
            if farthest < i:
                return False
            farthest = max(farthest, i+n)

            if farthest >= len(nums)-1:
                return True 

        return False