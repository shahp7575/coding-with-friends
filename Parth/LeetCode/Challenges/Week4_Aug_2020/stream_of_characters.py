"""
Using Trie data structure.

Runtime: 796 ms
Memory: 42.4 MB
"""

from typing import List
from collections import defaultdict

class TrieNode:

    def __init__(self):

        self.dict = defaultdict(TrieNode)
        self.is_word = False

class StreamChecker:

    """
    Problem Statement:
    Implement the StreamChecker class as follows:

    StreamChecker(words): Constructor, init the data structure with the given words.
    query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, 
    including this letter just queried) spell one of the words in the given list.
    """
    def __init__(self, words: List[str]):
        
        self.prefix = ''
        self.trie = TrieNode()

        for word in words:

            cur_node = self.trie

            word = word[::-1]

            for char in word:
                cur_node = cur_node.dict[char]

            cur_node.is_word = True

    def query(self, letter: str) -> bool:
        
        self.prefix += letter

        cur_node = self.trie

        for char in reversed(self.prefix):

            if char not in cur_node.dict:
                break
            
            cur_node = cur_node.dict[char]

            if cur_node.is_word:
                return True

        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

if __name__ == "__main__":

    words = ['cd', 'f', 'kl']
    result = StreamChecker(words)
    print(result.query('a'))
    print(result.query('b'))
    print(result.query('c'))
    print(result.query('d'))
    print(result.query('e'))
    print(result.query('f'))