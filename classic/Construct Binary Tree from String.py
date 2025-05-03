'''
https://www.lintcode.com/problem/880/
'''

from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param s: a string
    @return: a root of this tree
    """
    def str2tree(self, s: str) -> TreeNode:
        # write your code here
        n = len(s)
        i = 0

        def dfs():
            nonlocal i

            sign = 1
            if s[i] == '-':
                sign = -1
                i += 1
            
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            num *= sign

            root = TreeNode(num)

            if i < n and s[i] == '(':
                i += 1
                root.left = dfs()
                i += 1
            if i < n and s[i] == '(':
                i += 1
                root.right = dfs()
                i += 1
            return root
        return dfs()
