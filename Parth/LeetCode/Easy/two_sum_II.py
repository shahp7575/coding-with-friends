"""
Two pointer solution

Runtime: 56 ms
Memory: 14.3 MB
"""

from typing import List

class Solution:

    """
    Problem Statement:
    Given an array of integers that is already sorted in ascending order, 
    find two numbers such that they add up to a specific target number.
    The function twoSum should return indices of the two numbers such that they add up to the target, 
    where index1 must be less than index2.
    
    Input: [2,7,11,15]
    Output: [1,2]
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

if __name__ == "__main__":

    result = Solution()
    nums = [2,7,11,15]
    target = 9
    print(result.twoSum(nums, target))