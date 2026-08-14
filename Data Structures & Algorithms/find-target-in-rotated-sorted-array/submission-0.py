class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # 1. Find rotation offset
        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        offset = l

        # 2. Normal binary search in virtual sorted array
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2

            real_m = (m + offset) % n

            if nums[real_m] == target:
                return real_m
            elif nums[real_m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1