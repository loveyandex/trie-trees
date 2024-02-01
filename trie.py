class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.translation = None  # Additional information for the word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, translation):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.translation = translation

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False, None
            node = node.children[char]
        return node.is_end_of_word, node.translation

    def starts_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage:
trie = Trie()
trie.insert("سلام", {"english": "hello", "example": "سلام دنیا"})
trie.insert("خداحافظ", {"english": "goodbye", "example": "خداحافظ دوست عزیز"})
trie.insert("مرسی", {"english": "thank you", "example": "مرسی برای کمک"})

print(trie.search("سلام"))  # (True, {'english': 'hello', 'example': 'سلام دنیا'})
print(trie.search("خداحافظ"))  # (True, {'english': 'goodbye', 'example': 'خداحافظ دوست عزیز'})
print(trie.search("hello"))  # (False, None)
print(trie.starts_with_prefix("مر"))  # True
