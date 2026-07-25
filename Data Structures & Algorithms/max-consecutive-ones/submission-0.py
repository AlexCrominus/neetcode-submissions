class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        local = 0
        maxed = 0

        for n in nums:
            if n == 1:
                local +=1
            else:
                maxed = max(maxed, local)
                local = 0
        maxed = max(maxed, local)
        return maxed