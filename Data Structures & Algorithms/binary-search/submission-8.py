class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        m = len(nums)//2
        while nums[m] != target:
            m_bak = m


            if nums[m] > target:
                r = m
            else:
                l = m

            m = (l+r)//2
            if m_bak == m:
                return -1
        return m