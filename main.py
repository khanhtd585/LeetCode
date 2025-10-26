from typing import List
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        rs = []
        nums.sort()
        def recur(start, cur: List, total):
            if total > target or start == len(nums):
                return True
            if total == target:
                rs.append(cur.copy())
                return
            cur.append(nums[start])
            over = recur(start, cur,  total + nums[start])
            cur.pop()
            if not over:
                recur(start + 1, cur, total)
        recur(0, [], 0)
        return rs


sol = Solution()
nums = [2,3,6,7] 
target = 7
print(sol.combinationSum(nums, target))
