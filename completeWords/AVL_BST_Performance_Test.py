import random
import time
from AVL import AVLTree
from BST import BST

# Função para gerar uma lista de palavras aleatórias
def generate_random_words(n):
    words = []
    for _ in range(n):
        word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
        words.append(word)
    return words

# Função para medir o tempo de inserção em uma árvore
def measure_insertion_time(tree, words):
    start_time = time.time()
    for word in words:
        tree.add(word)
    end_time = time.time()
    return end_time - start_time

# Função para medir a altura da árvore
def measure_tree_height(tree):
    return tree.get_height()

# Função para medir o tempo de busca de palavras com prefixo
def measure_search_time(tree, prefix):
    start_time = time.time()
    result = tree.search_words_with_prefix(prefix)
    end_time = time.time()
    return end_time - start_time, len(result)

if __name__ == "__main__":
    # Número de palavras a serem inseridas
    num_words = 10000

    # Gere palavras aleatórias
    random_words = generate_random_words(num_words)

    # Crie instâncias das árvores AVL e BST
    avl_tree = AVLTree()
    bst_tree = BST()

    # Meça o tempo de inserção
    avl_insertion_time = measure_insertion_time(avl_tree, random_words.copy())
    bst_insertion_time = measure_insertion_time(bst_tree, random_words.copy())

    # Meça a altura das árvores
    avl_tree_height = measure_tree_height(avl_tree)
    bst_tree_height = measure_tree_height(bst_tree)

    # Prefixo de busca
    search_prefix = "abc"

    # Meça o tempo de busca com prefixo
    avl_search_time, avl_search_count = measure_search_time(avl_tree, search_prefix)
    bst_search_time, bst_search_count = measure_search_time(bst_tree, search_prefix)

    # Imprima os resultados
    print("Número de palavras inseridas:", num_words)
    print("Tempo de inserção AVL:", avl_insertion_time)
    print("Tempo de inserção BST:", bst_insertion_time)
    print("Altura da Árvore AVL:", avl_tree_height)
    print("Altura da Árvore BST:", bst_tree_height)
    print("Tempo de busca AVL (prefixo '{}'): {} segundos, {} palavras encontradas".format(search_prefix, avl_search_time, avl_search_count))
    print("Tempo de busca BST (prefixo '{}'): {} segundos, {} palavras encontradas".format(search_prefix, bst_search_time, bst_search_count))
