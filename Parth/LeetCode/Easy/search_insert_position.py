"""
Binary Search implementation. 

Runtime: 56 ms
Memory: 14.5 MB
"""

from typing import List

class Solution:

    """
    Problem Statement:
    Given a sorted array and a target value, return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.

    Input: [1,3,5,6], 5
    Output: 2
    Input: [1,3,5,6], 2
    Output: 1
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":

    result = Solution()
    nums = [1,3,5,6,9]
    target = 1
    print(result.searchInsert(nums ,target))