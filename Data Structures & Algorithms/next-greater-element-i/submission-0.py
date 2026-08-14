class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        gel = [-1] * len(nums2)

        idxs = collections.defaultdict(int)

        for i in range(len(nums2)-1, -1, -1):
            idxs[nums2[i]] = i

            while stack and nums2[stack[-1]] <= nums2[i]:
                stack.pop()

            if stack:
                gel[i] = nums2[stack[-1]]

            stack.append(i)


        ret = []
        for n in nums1:
            ret.append(gel[idxs[n]])

        return ret