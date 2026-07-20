import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        answer = r


        while l <= r:
            m = (l + r) // 2

            ban = 0
            for j in range(len(piles)):
                ban += math.ceil(float(piles[j])/m)
            print(ban, m)
            if ban <= h:
                r = m - 1
                answer = m

            elif ban > h:
                l = m + 1



        return answer