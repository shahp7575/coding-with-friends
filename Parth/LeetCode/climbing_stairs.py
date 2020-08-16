"""
Using Top-down memoization!

Runtime: 28 ms
Memory: 14 MB
"""

import sys

class Solution:

    """
    Problem Statement:
    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top
        1) 1 step + 1 step
        2) 2 steps
    """

    def __init__(self):
        self.dic = {1:1, 2:2}

    def climbStairs(self, n: int) -> int:
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return self.dic[n]


if __name__ == "__main__":

    result = Solution()
    n = 6
    print(result.climbStairs(n))