"""
Runtime: 28 ms
Memory: 14.1 MB
"""

class Solution(object):

    """
    Problem # 357
    Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
    """

    def countNumbersWithUniqueDigits(self, n):
    
        if n == 0:
            return 1
    
        total, start = 10, 9
    
        for i in range(1, n):
            
            start = start*(10-i)
            total += start
            print(start, total)
        return total


if __name__ == "__main__":

    result = Solution()
    n = 3
    print(result.countNumbersWithUniqueDigits(n))