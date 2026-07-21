class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [((float(points[i][0]*points[i][0]+points[i][1]*points[i][1])/2), i) for i in range(len(points))]

        heapq.heapify(heap)

        ret = []

        for _ in range(k):
            ret.append(points[heapq.heappop(heap)[1]])

        return ret