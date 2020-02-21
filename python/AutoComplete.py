import sys
from   utils.io      import read_file
from   utils.ui.trie import run

class TrieNode:
    def __init__(self):
        self.letters = dict()
        self.is_end = False

    def list_all(self, value: str, ans: list) -> None:
        if self.is_end:
            ans.append(value)
        for c, next_node in self.letters.items():
            if next_node: next_node.list_all(value + c, ans)

class Trie:
    def __init__(self):
        self._root = TrieNode()

    def insert(self, *args) -> None:
        for word in args:
            curr_node = self._root
            for c in word:
                next_node = curr_node.letters.get(c, None)
                if not next_node:
                    curr_node.letters[c] = next_node = TrieNode()
                curr_node = next_node
            curr_node.is_end = True

    def find(self, word: str) -> TrieNode:
        curr_node = self._root
        for c in word:
            curr_node = curr_node.letters.get(c, None)
            if not curr_node: break
        return curr_node

    def find_all(self, word: str) -> list:
        ans = []
        node = self.find(word)
        if node: node.list_all(word, ans)
        return ans

def main() -> int:
    trie = Trie()
    trie.insert(*[line.strip() for line in read_file(sys.argv[1]).split('\n')])
    return run(trie)

if __name__ == '__main__': sys.exit(main())