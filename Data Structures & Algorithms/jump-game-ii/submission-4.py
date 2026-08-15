class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        jumps = 0
        mostPot = 0

        if len(nums) == 1:
            return 0
        

        for i,n in enumerate(nums):
            if farthest < i:
                farthest = mostPot
                jumps += 1
            if farthest < i+n:
                mostPot = max(mostPot, i+n)


            if farthest >= len(nums)-1:
                return jumps

        return jumps