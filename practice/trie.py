from queue import LifoQueue


class Node:
    def __init__(self):
        self.nodes = dict()
        self.is_word = False
        
class TRIE:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word, currnode=None):
        
        if not currnode:
            currnode = self.root
        
        if len(word) == 0:
            currnode.is_word = True
            return
        
        c = word[0]
        
        if c in currnode.nodes:
            self.insert(word[1:], currnode.nodes[c])
        else:
            currnode.nodes[c] = Node()
            self.insert(word[1:], currnode.nodes[c])
    
    def exists(self, word, currnode=None):
        if not currnode:
            currnode = self.root
        
        if len(word) == 0:
            return False, False
        
        if len(word) == 1:
            if word[0] in currnode.nodes:
                if currnode.nodes[word[0]].is_word:
                    return True, True
                return True, False
        
            return False, False

        c = word[0]
        
        if c in currnode.nodes:
            return self.exists(word[1:], currnode.nodes[c])
        
        return False, False
    
    def _explore(self, currnode):
        
        if len(currnode.nodes) == 0:
            return ""
        
        paths = []
        for c in currnode.nodes.keys():
            path = self._explore(currnode.nodes[c])
            if isinstance(path, str):
                paths.append(c + path)
            elif isinstance(path, list):
                path.insert(0, c)
                paths.append("".join(path))
        
        return paths
        
    
    def startsWith(self, word, currnode=None):
        
        '''
                                    g
                                    |
                                    r
                        -------------------------
                        |   |       |            |
                        e   a       o            a
                        |
                      -----
                      |   | 
                      e   a   
                
        '''
        
        root_word = word
        
        if not currnode:
            currnode = self.root
        
        while True:
            
            if len(word) == 0:
                break
            
            c = word[0]
            if c in currnode.nodes.keys():
                currnode = currnode.nodes[c]
                word = word[1:]
            else:
                break
        
        explored = self._explore(currnode)
        explored = [root_word + x for x in explored]
        
        return explored

        
        
if __name__ == "__main__":
    
    words = [
        'cat',
        'eat',
        'eaten',
        'apple',
        'app',
        'great',
        'grate',
        'ear',
        'ape',
        'cast',
        'eatery',
        'green',
        'grow'
    ]
    
    tree = TRIE()
    
    for word in words:
        tree.insert(word)
    
    print(tree.startsWith('gr'))
    