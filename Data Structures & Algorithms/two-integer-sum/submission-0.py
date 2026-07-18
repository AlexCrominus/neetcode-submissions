class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, numi in enumerate(nums):
            for j, numj in enumerate(nums[i+1:]):
                print(numi, numj)
                if numi + numj == target:
                    return [i, j+i+1]

        return []