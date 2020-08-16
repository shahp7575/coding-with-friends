"""
Runtime: 64 ms
Memory: 13.8 MB
"""

from typing import List

class Solution:

    """
    Problem Statement:
    Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

    The digits are stored such that the most significant digit is at the head of the list,
    and each element in the array contains a single digit.

    You may assume the integer does not contain any leading zero, except the number 0 itself.

    Input: [1,2,3]
    Output: [1,2,4]
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        
        len_digits = len(digits) - 1
        number = 0
        for dig in digits:
            number = number + dig * 10**len_digits
            len_digits -= 1

        number += 1
        return [int(i) for i in str(number)]

if __name__ == "__main__":

    result = Solution()
    digs = [4,3,1,9]
    print(result.plusOne(digs))