from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow, fast, nums[slow], nums[fast])
            if slow == fast:
                break
        print()
        slow1 = 0
        while True:
            slow = nums[slow]
            slow1 = nums[slow1]
            print(slow1, slow)
            if slow == slow1:
                break   
        return slow
    
sol = Solution()
nums = [1,2,3,4,5,6,7,8,7,7,9,10,7]
print(sol.findDuplicate(nums))
