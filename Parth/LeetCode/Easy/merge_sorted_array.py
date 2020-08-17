"""
Runtime: 40 ms
Memory: 13.8 MB
"""

from typing import List

class Solution:

    """
    Problem Statement:
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(1,n+1):
            nums1[-i] = nums2[i-1]
            #nums1[:-i] = nums2[i-1]

        nums1[:] = sorted(nums1)

if __name__ == "__main__":

    result = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3
    result.merge(nums1, 3, nums2, n)