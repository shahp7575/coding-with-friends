"""
Runtime: 88 ms
Memory: 15.4 MB
"""

from typing import List

class Solution:

    """
    Problem #34
    Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        i = 0
        j = -1
        count_i = 0
        count_j = 0
        ans = []
        if target not in nums:
            return [-1,-1]
        else:
            for num in nums:
                if nums[i] == target and count_i == 0:
                    ans.append(i)
                    count_i += 1
                if nums[j] == target and count_j == 0:
                    ans.append(len(nums) + j)
                    count_j += 1
                i += 1
                j -= 1
        return sorted(ans)


if __name__ == "__main__":

    result = Solution()
    nums = [1]
    target = 1
    print(result.searchRange(nums, target))
        