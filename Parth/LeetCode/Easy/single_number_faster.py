"""
Fantastic Bit Manipulation Solution.

- If we take XOR of zero and soem bit, it will return that bit
    a XOR 0 = a

- If we take XOR of two same bits, it will return 0
    a XOR a = 0

- a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b

So we can XOR all bits together to find the unique number

Runtime: 80 ms (4800+ ms with set)
Memory: 16.5 MB (16.2 MB with set)
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

    a = 0
    for i in nums:
        a ^= i
    
    return a

if __name__ == "__main__":

    result = Solution()
    nums = [4,1,2,1,2]
    print(result.singleNumber(nums))