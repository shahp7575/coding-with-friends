"""
Runtime: 52 ms
Memory: 14.4 MB
"""

class Solution:

    """
    Problem Statement:
    Given a string, you need to reverse the order of characters in 
    each word within a sentence while still preserving whitespace and initial word order.
    """

    def reverseWords(self, s: str) -> str:

        return " ".join([w[::-1] for w in s.split()])

if __name__ == "__main__":

    result = Solution()
    test_str = "Let's take LeetCode contest"
    print(result.reverseWords(test_str)) 