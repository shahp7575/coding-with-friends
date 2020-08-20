"""
Runtime: 296 ms
Memory: 15.2 MB
"""

from typing import List

class Solution:

    """
    Problem Statement:
    Given an array of size n, find the majority element. 
    The majority element is the element that appears more than ⌊ n/2 ⌋ times.

    Input: [3,2,3]
    Output: 3
    """

    def majorityElement(self, nums: List[int]) -> int:

        for num in set(nums):
            if nums.count(num) > len(nums)/2:
                return num

if __name__ == "__main__":
    
    result = Solution()
    nums = [3,2,3]
    print(result.majorityElement(nums))