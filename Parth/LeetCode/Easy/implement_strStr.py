"""
Leveraging the string.find() function.

Runtime: 24 ms
Memory Usage: 14.1 MB
"""

class Solution:

    """
    Problem Statement:
    Return the index of the first occurrence of needle in haystack, 
    or -1 if needle is not part of haystack.

    Input: haystack = "hello", needle="ll"
    Output: 2
    """

    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) > 0:
            if needle in haystack:
                return haystack.find(needle)
            else:
                return -1
        else:
            return 0


if __name__ == "__main__":

    result = Solution()
    haystack = "hello"
    needle = "or"
    print(result.strStr(haystack, needle))