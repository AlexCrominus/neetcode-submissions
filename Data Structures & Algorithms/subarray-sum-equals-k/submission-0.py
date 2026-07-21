class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ret = 0
        prefix_sum = 0
        sums = {0: 1}

        for num in nums:
            prefix_sum += num

            ret += sums.get(prefix_sum - k, 0)

            sums[prefix_sum] = 1 + sums.get(prefix_sum, 0)

        return ret
        