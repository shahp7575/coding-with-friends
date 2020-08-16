"""
Runtime: 28 ms
Memory Usage: 13.9 MB
"""

from typing import List

class Solution:

    """
    Problem Statement:
    Given an array nums and a value val, 
    remove all instances of that value in-place and return the new length.

    Do not allocate extra space for another array, you must do this by 
    modifying the input array in-place with O(1) extra memory.

    The order of elements can be changed. It doesn't matter what you leave
    beyond the new length.
    """

    def removeElement(self, nums: List[int], val: int) -> int:

        count_val = nums.count(val)

        for i in range(count_val):
            nums.remove(val)

        return len(nums)


if __name__ == "__main__":

    result = Solution()
    numbers = [0,1,2,2,3,0,4,2]
    val = 2
    print(result.removeElement(numbers, val))