class Solution:



    def backspaceCompare(self, S: str, T: str) -> bool:

        return S == T

if __name__ == "__main__":

    result = Solution()
    S = "ab#c"
    T = "ad#c"
    print(result.backspaceCompare(S, T))
        