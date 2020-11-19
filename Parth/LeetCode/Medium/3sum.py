"""
Runtime: 684 ms
Memory: 18.9 MB
"""

from typing import List

class Solution:

    """
    Problem #15:
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

    Notice that the solution set must not contain duplicate triplets.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            print(i, v)
            
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                print("X: ", x)
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
            print("D: ", d)
            print("Res: ", res)
            print()
        return list(map(list, res))

if __name__ == "__main__":

    result = Solution()
    nums = [-1,0,1,2,-1,-4]
    #nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
    #nums = [1,-1,-1,0]
    print(result.threeSum(nums))