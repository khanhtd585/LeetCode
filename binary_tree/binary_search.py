from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1
    
nums=[-1,0,3,5,9,12]
target=9

# nums = [-1,0,2,4,6,8]
# target = 3

# nums = [-1,0,2,4,6,8]
# target = 4
col = Solution()
print(col.search(nums, target))