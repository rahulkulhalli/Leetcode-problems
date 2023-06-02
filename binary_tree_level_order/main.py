from typing import List, Optional
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(current, explored):
            if current.empty():
                return explored
            
            # fetch the first element off the queue.
            node = current.get()

            if node:
                # push the value into the explored list.
                explored.append(node.val)
            
                # push the child nodes on the queue.
                current.put(node.left)
                current.put(node.right)
            
            return bfs(current, explored)
        
        output = []
        
        if not root:
            return output
        
        current, explored = Queue(), list()
        
        current.put(root)
        
        # Push the root on the queue.
        bfs_list = bfs(current, explored)

        if len(bfs_list) == 2:
            return [[bfs_list[1]], [bfs_list[0]]]
        
        output = []
        i = len(bfs_list)-2
        while i > 0:
            interm = bfs_list[i:i+2]
            output.append(interm)
            i -= 2
        
        output.append([bfs_list[0]])
        
        return output


def makeTree():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    
    # root = None
    
    return root


if __name__ == "__main__":
    tree = makeTree()
    op = Solution().levelOrderBottom(tree)
    print(op)