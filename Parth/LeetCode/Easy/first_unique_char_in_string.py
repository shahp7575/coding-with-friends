"""
Runtime: 5336 ms
Memory: 13.9 MB
"""

class Solution:

    """
    Given a string, find the first non-repeating character in it and return its index. 
    If it doesn't exist, return -1.
    """

    def firstUniqChar(self, s: str) -> int:
        
        for i, char in enumerate(s):
            if s.count(char) == 1:
                return i

        return -1

if __name__ == "__main__":

    result = Solution()
    test_str = "codecode"
    print(result.firstUniqChar(test_str))
        