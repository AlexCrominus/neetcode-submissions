class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        copy = nums.copy()
        nums.extend(copy)
        return nums 