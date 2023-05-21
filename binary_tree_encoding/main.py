from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class BTree:
    def __init__(self, rootval):
        self.root = TreeNode(rootval)
    
    def insert(self, val, node=None):
        if node is None:
            node = self.root
        
        if val <= node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self.insert(val, node.left)
        
        if val > node.val:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self.insert(val, node.right)
                


class Codec:

    def _bfs(self, visited, explored=[]):
        if visited.empty():
            return explored

        # Pop the first element off the visited stack.
        node = visited.get()
        
        explored.append(node.val)
        
        if node.left is not None:
            visited.put(node.left)
        if node.right is not None:
            visited.put(node.right)
        
        return self._bfs(visited, explored)
        
        
    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        """
        
        visited = Queue()
        explored = list()
        
        visited.put(root)
        
        traversed = self._bfs(visited, explored)
        return ",".join([str(x) for x in traversed])


    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        """
        
        values = [int(x) for x in data.split(",")]
        
        root = TreeNode(values[0])
        
        ix = 0
        while (ix + 3) < len(values):
            current = TreeNode(values[ix])
            current.left = TreeNode(values[ix+1])
            current.right = TreeNode(values[ix+2])
            
            ix += 3
            


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(8)
    
    '''
                         10
                        /  \
                       5    12
                      /\
                     3  8
    '''
    
    codec = Codec()
    print(codec.serialize(root))
    