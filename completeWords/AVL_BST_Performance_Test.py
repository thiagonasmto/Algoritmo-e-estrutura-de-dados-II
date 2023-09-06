import random
import time
from AVL import AVLTree
from BST import BST
import matplotlib.pyplot as plt

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

# Função para plotar os resultados
def plot_results(avl_insertion_time, bst_insertion_time, avl_tree_height, bst_tree_height,
                 avl_search_time, avl_search_count, bst_search_time, bst_search_count):
    labels = ['AVL', 'BST']
    insertion_times = [avl_insertion_time, bst_insertion_time]
    tree_heights = [avl_tree_height, bst_tree_height]
    search_times = [avl_search_time, bst_search_time]
    search_counts = [avl_search_count, bst_search_count]

    # Plotando os resultados
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

    # Gráfico de Tempo de Inserção
    axes[0, 0].bar(labels, insertion_times, color=['blue', 'green'])
    axes[0, 0].set_xlabel('Árvore')
    axes[0, 0].set_ylabel('Tempo de Inserção (s)')
    axes[0, 0].set_title('Tempo de Inserção nas Árvores AVL e BST')

    # Gráfico de Altura das Árvores
    axes[0, 1].bar(labels, tree_heights, color=['blue', 'green'])
    axes[0, 1].set_xlabel('Árvore')
    axes[0, 1].set_ylabel('Altura da Árvore')
    axes[0, 1].set_title('Altura das Árvores AVL e BST')

    # Gráfico de Tempo de Busca
    axes[1, 0].bar(labels, search_times, color=['blue', 'green'])
    axes[1, 0].set_xlabel('Árvore')
    axes[1, 0].set_ylabel('Tempo de Busca (s)')
    axes[1, 0].set_title('Tempo de Busca nas Árvores AVL e BST')

    # Gráfico de Número de Palavras Encontradas na Busca
    axes[1, 1].bar(labels, search_counts, color=['blue', 'green'])
    axes[1, 1].set_xlabel('Árvore')
    axes[1, 1].set_ylabel('Número de Palavras Encontradas')
    axes[1, 1].set_title('Número de Palavras Encontradas na Busca nas Árvores AVL e BST')

    plt.tight_layout()

    plt.show()

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
    search_prefix = "a"

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
    print("Tempo de busca BST (prefixe '{}'): {} segundos, {} palavras encontradas".format(search_prefix, bst_search_time, bst_search_count))

    # Plotar os resultados
    plot_results(avl_insertion_time, bst_insertion_time, avl_tree_height, bst_tree_height,
                 avl_search_time, avl_search_count, bst_search_time, bst_search_count)
