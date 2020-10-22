"""
Runtime: 80 ms
Memory: 14.6 MB
"""

from typing import List

class Solution:

    """
    Problem #131:
    Given a string s, partition s such that every substring of the partition is a palindrome.

    Return all possible palindrome partitioning of s.

    Input: "aab"
    Output:
        [
            ["aa","b"],
            ["a","a","b"]
        ]
    """

    def partition(self, s: str) -> List[List[str]]:

        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):

        if not s:
            res.append(path)
            return

        for i in range(1, len(s)+1):

            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)

    def isPalindrome(self, s):
        return s == s[::-1]
       


if __name__ == "__main__":

    result = Solution()
    s = 'aab'
    print(result.partition(s))