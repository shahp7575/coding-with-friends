"""
Using python's in-built split function.

Runtime: 28 ms
Memory Usage: 13.8 MB
"""

class Solution:

    """
    Problem Statement: Given a string s consists of upper/lower-case alphabets and 
    empty space characters ' ', return the length of last word 
    (last word means the last appearing word if we loop from left to right) 
    in the string.

    If the last word does not exist, return 0.
    """

    def lengthOfLastWord(self, s: str) -> int:
        
        s_split = s.split()

        if len(s_split) > 0:
            return len(s_split[-1])
        else:
            return 0

if __name__ == "__main__":
    result = Solution()
    print(result.lengthOfLastWord('Hello World'))