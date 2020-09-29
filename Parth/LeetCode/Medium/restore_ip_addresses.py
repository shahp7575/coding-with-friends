"""
Runtime: 344 ms
Memory: 14.2 MB
"""

from typing import List

class Solution:

    """
    Problem Statement:
    Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. 
    You can return them in any order.
    A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and 
    cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 
    """



    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        self.dfs(s, 0, "", res)
        return res

    def dfs(self, s, idx, path, res):

        if idx > 4:
            return
        if idx == 4 and not s:
            res.append(path[:-1])
        for i in range(1, len(s) + 1):
            if s[:i] == '0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
                 self.dfs(s[i:], idx+1, path+s[:i]+".", res)

if __name__ == "__main__":

    result = Solution()
    s = "25525511135"
    print(result.restoreIpAddresses(s))