"""
Runtime: 136 ms
Memory: 33 MB
"""
from typing import List

class Solution:

    """
    Problem Statement:
    Given an array, rotate the array to the right by k steps, where k is non-negative.

    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        if k > 0:
            nums[:] = eval(str(nums[-k:] + nums[:len(nums)-k]))
        else:
            return nums
        return nums

if __name__ == "__main__":

    result = Solution()
    nums = [1,2,3,4,5,6]
    k = 11
    print(result.rotate(nums, k))