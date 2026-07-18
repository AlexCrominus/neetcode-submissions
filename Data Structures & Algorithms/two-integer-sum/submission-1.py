class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {}

        for i, num in enumerate(nums):
            secondNum = target - num
            if secondNum in prevMap:
                return [prevMap[secondNum], i]
            prevMap[num] = i
            