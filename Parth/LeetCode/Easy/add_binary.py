"""
Runtime: 24 ms
Memory: 13.6 MB
"""

class Solution:

    """
    Given two binary strings, return their sum (also a binary string).

    The input strings are both non-empty and contains only characters 1 or 0.
    """

    def addBinary(self, a: str, b: str) -> str:
        
        sums = int(a, 2) + int(b, 2)
    
        return (bin(sums))[2:]


if __name__ == "__main__":

    result = Solution()
    a = "1010"
    b = "1011"
    print(result.addBinary(a, b))