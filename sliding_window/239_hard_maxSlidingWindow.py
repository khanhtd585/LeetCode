from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        rs = []
        l, r = 0, k
        pos_max = -1
        while r <= len(nums):
            if pos_max >= l:
                if nums[pos_max] < nums[r - 1]:
                    pos_max = r - 1
            else:
                pos_max = l
                for i in range(l,r):
                    if nums[i] >= nums[pos_max]:
                        pos_max = i
                        
            rs.append(nums[pos_max])
            l += 1
            r += 1
        return rs
    
sol = Solution()
nums = [1,2,1,0,4,2,6]
k = 3
print(sol.maxSlidingWindow(nums, k))