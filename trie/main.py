'''
208. Implement Trie (Prefix Tree): https://leetcode.cn/problems/implement-trie-prefix-tree/
'''

import collections


class Trie:

    def __init__(self):
        trie = lambda: collections.defaultdict(trie)
        self.root = trie()

    def insert(self, word: str) -> None:
        p = self.root
        for ch in word:
            p = p[ch]
        p[None] = True

    def search(self, word: str) -> bool:
        p = self.root
        for ch in word:
            if ch not in p:
                return False
            p = p[ch]
        return p[None] == True
        

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for ch in prefix:
            if ch not in p:
                return False
            p = p[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
