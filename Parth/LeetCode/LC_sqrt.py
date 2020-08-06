"""
Trying a very simple approach.

Runtime: 40 ms
Memory Usage: 14.1 MB
"""

class Solution:

    """
    Problem Statement: Compute and return the square root of x, 
    where x is guaranteed to be a non-negative integer.
    """

    def mySqrt(self, x: int) -> int:

        # power raise to 0.5
        result = x ** (1/2)

        return int(result)

if __name__ == "__main__":
    result = Solution()
    print(result.mySqrt(x=10202))