"""
Runtime: 24 ms
Memory: 15.5 MB
"""

class Solution:

    """
    Problem Statement:
    Given a sentence text (A sentence is a string of space-separated words) in the following format:

    First letter is in upper case.
    Each word in text are separated by a single space.
    Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths.
    """

    def arrangeWords(self, text: str) -> str:

        words = text.split()

        sorted_words =  sorted(words, key=lambda x: len(x))

        return sorted_words[0].title() + " " + " ".join(sorted_words[1:]).lower()

if __name__ == "__main__":

    result = Solution()
    text = "Keep calm and code on"
    print(result.arrangeWords(text)) 