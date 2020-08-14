"""
Runtime: 72 ms
Memory Usage: 15.6 MB

Note: The difference between nums[:]= and nums = is that the latter doesn't replace
elements in the original list.
"""

from typing import List


class Solution:

    """
    Problem Statement:
    Given a sorted array nums, remove the duplicates in-place such that 
    each element appear only once and return the new length.
    Do not allocate extra space for another array, you must do this by modifying 
    the input array in-place with O(1) extra memory.
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        
        nums[:] = sorted(set(nums))
        print(nums)
        return len(nums)


if __name__ == "__main__":

    result = Solution()
    list_nums = [1,1,2]
    result.removeDuplicates(list_nums)