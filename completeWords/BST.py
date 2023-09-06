import text_processing  # Importa um módulo chamado 'text_processing', se necessário.

class Node:
    def __init__(self, value):
        self.value = value  # Inicializa um nó com um valor e sem filhos.
        self.left_child = None
        self.right_child = None

class BST:
    def __init__(self):
        self.root = None  # Inicializa uma árvore binária de busca (BST) vazia com raiz nula.

    def add(self, value):
        if self.root is None:  # Se a árvore estiver vazia, cria a raiz com o valor.
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)  # Caso contrário, chama a função de adição recursiva.

    def _add_recursive(self, current_node, value):
        if value <= current_node.value:  # Compara o valor a ser adicionado com o valor do nó atual.
            if current_node.left_child is None:  # Se não houver filho esquerdo, cria um nó com o valor.
                current_node.left_child = Node(value)
            else:
                self._add_recursive(current_node.left_child, value)  # Caso contrário, continua a busca à esquerda.
        else:
            if current_node.right_child is None:  # Se não houver filho direito, cria um nó com o valor.
                current_node.right_child = Node(value)
            else:
                self._add_recursive(current_node.right_child, value)  # Caso contrário, continua a busca à direita.

    def _contains(self, current_node, value):
        if current_node is None:
            return False  # Se o nó atual for nulo, o valor não foi encontrado.
        if current_node.value == value:
            return True  # Se o valor do nó atual for igual ao valor procurado, o valor foi encontrado.
        if value < current_node.value:
            return self._contains(current_node.left_child, value)  # Busca à esquerda.
        return self._contains(current_node.right_child, value)  # Busca à direita.

    def contains(self, value):
        return self._contains(self.root, value)  # Chama a função de busca a partir da raiz.

    def search_words_with_prefix(self, prefix):
        words = []  # Inicializa uma lista para armazenar palavras com o prefixo.
        self._search_words_with_prefix_recursive(self.root, prefix, '', words)
        return words  # Retorna a lista de palavras encontradas.

    def _search_words_with_prefix_recursive(self, current_node, prefix, current_word, words):
        if current_node is None:
            return  # Se o nó atual for nulo, encerra a recursão.

        current_word += current_node.value  # Adiciona o valor do nó atual à palavra atual.

        # Verifique se a string em current_node.value começa com o prefixo.
        if current_node.value.startswith(prefix):
            words.append(current_node.value)  # Se sim, adiciona a palavra à lista.

        # Continue a busca nas subárvores esquerda e direita.
        self._search_words_with_prefix_recursive(current_node.left_child, prefix, current_word, words)
        self._search_words_with_prefix_recursive(current_node.right_child, prefix, current_word, words)

    # Atualiza a função get_height
    def get_height(self):
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, current_node):
        if current_node is None:
            return 0  # Se o nó atual for nulo, a altura é zero.

        left_height = self._get_height_recursive(current_node.left_child)  # Altura da subárvore esquerda.
        right_height = self._get_height_recursive(current_node.right_child)  # Altura da subárvore direita.

        # A altura da árvore é o máximo entre a altura da subárvore esquerda e direita + 1.
        return max(left_height, right_height) + 1
