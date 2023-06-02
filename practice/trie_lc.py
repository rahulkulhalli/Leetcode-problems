class Node:
    def __init__(self):
        self.nodes = dict()
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def _insert(self, word, node):
        if not node:
            node = self.root
        
        if len(word) == 0:
            node.is_word = True
            return
        
        c = word[0]

        if c in node.nodes:
            self._insert(word[1:], node.nodes[c])
        else:
            node.nodes[c] = Node()
            self._insert(word[1:], node.nodes[c])

    def insert(self, word: str) -> None:

        if len(word) == 0:
            return
        
        self._insert(word, None)

    def search(self, word: str) -> bool:
        # search will only return true if the entire word matches.

        if len(word) == 0:
            return False
        
        runner = self.root
        
        for ch in word:
            if ch not in runner.nodes.keys():
                return False
        
            runner = runner.nodes[ch]
        
        # print(runner.nodes)
        
        if runner.is_word:
            return True
        
        return False


    def startsWith(self, prefix: str) -> bool:
        
        if len(prefix) == 0:
            return False
        
        runner = self.root

        for ch in prefix:
            if ch not in runner.nodes.keys():
                return False
            runner = runner.nodes[ch]
        
        return True



if __name__ == "__main__":
    obj = Trie()
    obj.insert("apple")
    print(obj.search("apple"))
    print(obj.startsWith("app"))