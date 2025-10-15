from typing import List
import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hip = []
        for p in points:
            x, y = p[0], p[1]
            distance = (math.sqrt(x**2 + y**2))
            hip.append((distance, x, y))

        heapq.heapify(hip)
        rs = []
        for _ in range(k):
            _, x, y = heapq.heappop(hip)
            rs.append([x,y])
        return rs


sol = Solution()
points=[[0,2],[2,2]]
k=1

points=[[3,3],[5,-1],[-2,4]]
k=2
print(sol.kClosest(points, k))


