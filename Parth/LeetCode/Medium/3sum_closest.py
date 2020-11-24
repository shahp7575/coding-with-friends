"""INCOMPLETE"""

from typing import List

class Solution:

    """

    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        diff = sum(nums[:3]) - target
        
        print(diff)
        for i in range(len(nums)):

            if len(nums[i:i+3]) == 3 and abs(sum(nums[i:i+3]) - target) <= abs(diff):

                ans = sum(nums[i:i+3])

            elif len(nums[i:i+3]) != 3:
                break
            
        return ans


if __name__ == "__main__":

    result = Solution()
    nums = [0,2,1,-3]
    target = 1
    print(result.threeSumClosest(nums, target))