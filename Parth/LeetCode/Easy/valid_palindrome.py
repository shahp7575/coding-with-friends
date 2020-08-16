"""
Runtime: 52 ms
Memory: 19.6 MB
"""

class Solution:

    """
    Problem Statement:
    Given a string, determine if it is a palindrome, 
    considering only alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid palindrome.

    Input: "A man, a plan, a canal: Panama"
    Output: true
    """

    def isPalindrome(self, s: str) -> bool:
        
        real_str = [char.lower() for char in s if char.isalpha() or char.isdigit()]

        return real_str == real_str[::-1]


if __name__ == "__main__":

    result = Solution()
    test_string = "A man, a plan, a canal: Panama"
    print(result.isPalindrome(test_string))