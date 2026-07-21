class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-a for a in stones]
        heapq.heapify(stones)

        while len(stones) != 1 and len(stones) != 0:
            val1 = heapq.heappop(stones)
            val2 = heapq.heappop(stones)
            print(val1, val2)


            if val1 == val2:
                continue
            elif val1 < val2:
                heapq.heappush(stones, -val2+val1)
            else:
                heapq.heappush(stones, -val1+val2)

        if len(stones) == 0:
            return 0
        return -stones[0]