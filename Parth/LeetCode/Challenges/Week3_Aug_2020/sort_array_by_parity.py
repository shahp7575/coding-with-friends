"""
Runtime: 80 ms
Memory: 14.4 MB
"""

from typing import List

class Solution:

    """
    Problem Statement:
    Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

    You may return any answer array that satisfies this condition.
    """

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        odd = []
        even = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        return even + odd
        

if __name__ == "__main__":

    result = Solution()
    A = [3,1,2,4]
    print(result.sortArrayByParity(A))