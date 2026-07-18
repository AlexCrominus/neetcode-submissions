class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numsMap = {}

        for num in nums:

            numsMap[num] = 1 + numsMap.get(num, 0)

        return sorted(numsMap, key=numsMap.get)[len(numsMap)-k:]

