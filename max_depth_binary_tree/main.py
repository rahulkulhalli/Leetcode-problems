from queue import Queue
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(currnode):
            if not currnode:
                return 0
            
            l_depth, r_depth = 0, 0
            if currnode.left:
                l_depth = dfs(currnode.left)
            if currnode.right:
                r_depth = dfs(currnode.right)
            
            return 1 + max(l_depth, r_depth)
        
        return dfs(root)


def makeTree():
    root = TreeNode(3)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)
    
    root.right = TreeNode(2)
    
    return root


if __name__ == "__main__":
    tree = makeTree()
    s = Solution()
    print(s.maxDepth(tree))