from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        trap = 0
        maxL, maxR = height[l], height[r]
        while l < r:
            if maxR < maxL:
                r -= 1
                maxR = max(maxR, height[r])
                trap += max(0, (maxR - height[r]))
            else:
                l += 1
                maxL = max(maxL, height[l])
                trap += max(0, (maxL - height[l]))
        return trap
    

sol = Solution()
height = [0,2,0,3,1,0,1,3,2,1]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))