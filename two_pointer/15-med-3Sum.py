from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rs = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i-1]:
                continue
            le, ri = i + 1, len(nums) - 1
            while le < ri:
                three_sum = n + nums[le] + nums[ri]
                print(n, nums[le] , nums[ri])
                if three_sum > 0:
                    ri -= 1
                elif three_sum < 0:
                    le += 1
                else:
                    rs.append([n, nums[le], nums[ri]])
                    ri -= 1
                    le += 1
                    while nums[le] == nums[le-1] and le < ri:
                        le += 1
        return rs

nums=[-2,0,0,2,2]
solution = Solution()
print(solution.threeSum(nums))
