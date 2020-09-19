from typing import List

"""
Runtime: 392 ms
Memory: 21.4 MB
"""

class Solution:

    """
    Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
    Find all the elements that appear twice in this array.
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:

        res = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return res

if __name__ == "__main__":

    result = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(result.findDuplicates(nums))