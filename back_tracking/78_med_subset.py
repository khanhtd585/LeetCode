from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rs = []
        limit = len(nums)
        def recur(ns: List, start: int):
            rs.append(ns)
            if start == limit:
                return
            for i in range(start, limit):
                recur(ns + [nums[i]], i + 1)
                
        recur([], 0)
        return rs
        
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]

        return res
    
sol = Solution()
nums = [7]
nums = [1,2,3]
print(sol.subsets(nums))