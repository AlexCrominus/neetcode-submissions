class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        count = 0
        for n in nums:
            if n != 0:
                prod *= n
            else:
                count += 1

        ret = []

        for n in nums:
            if count > 1:
                ret.append(0)

            elif n == 0 and count == 1:
                ret.append(prod)
            elif n!= 0 and count ==1:
                ret.append(0)
            else:
                ret.append(prod//n)

        return ret
        