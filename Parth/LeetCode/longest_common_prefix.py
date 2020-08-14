"""
Using vertical scanning to fetch same index character for each string in array.
If their set() length == 1, then only move to the next character; else break.

Runtime: 28 ms
Memory Usage: 13.9 MB
"""

from typing import List

class Solution:
   
    """
    Problem Statement:Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    Input: ["flower", "flow", "flight"]
    Output: "fl"

    Input: ["dog", "racecar", "car"]
    Output: ""
    """
   
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        chars = []

        for i in zip(*strs):
            if len(set(i)) == 1:
                chars.append("".join(set(i)))
            else:
                break

        return "".join(chars)

    
if __name__ == "__main__":

    result = Solution()
    test_str = ['joy', 'joyful', 'jogging', 'jolly', 'jogger']

    print(result.longestCommonPrefix(test_str))