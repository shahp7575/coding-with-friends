"""
Using set!

Runtime: 4824 ms (SLOW)
Memory: 16.2 MB
"""

from typing import List

class Solution:

    """
    Problem Statement:
    Given a non-empty array of integers, every element appears twice except for one. 
    Find that single one.

    Note:
    Your algorithm should have a linear runtime complexity. 
    Could you implement it without using extra memory?

    Input: [2,2,1]
    Output: 1
    """

    def singleNumber(self, nums: List[int]) -> int:
        
        set_nums = set(nums)

        for num in set_nums:
            if nums.count(num) == 1:
                return num

if __name__ == "__main__":

    result = Solution()
    nums = [4,1,2,1,2]
    print(result.singleNumber(nums))