import text_processing

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, current_node, value):
        if value <= current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._add_recursive(current_node.left_child, value)
        else:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._add_recursive(current_node.right_child, value)

    def _contains(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._contains(current_node.left_child, value)
        return self._contains(current_node.right_child, value)

    def contains(self, value):
        return self._contains(self.root, value)
    
    def search_words_with_prefix(self, prefix):
        words = []
        self._search_words_with_prefix_recursive(self.root, prefix, '', words)
        return words

    def _search_words_with_prefix_recursive(self, current_node, prefix, current_word, words):
        if current_node is None:
            return

        current_word += current_node.value

        # Verifique se a string em current_node.value começa com o prefixo
        if current_node.value.startswith(prefix):
            words.append(current_node.value)

        # Continue a busca nas subárvores esquerda e direita
        self._search_words_with_prefix_recursive(current_node.left_child, prefix, current_word, words)
        self._search_words_with_prefix_recursive(current_node.right_child, prefix, current_word, words)
    
    #updade get_height
    def get_height(self):
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, current_node):
        if current_node is None:
            return 0

        left_height = self._get_height_recursive(current_node.left_child)
        right_height = self._get_height_recursive(current_node.right_child)

        # A altura da árvore é o máximo entre a altura da subárvore esquerda e direita + 1
        return max(left_height, right_height) + 1