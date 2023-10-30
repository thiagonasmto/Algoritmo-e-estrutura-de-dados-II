import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do arquivo de arestas
G = nx.read_edgelist('./small_worlds/data/facebook_combined.txt', nodetype=int)

# Obtenha o número de vértices (nós) no grafo
num_vertices = G.number_of_nodes()
print(f"Número de vértices: {num_vertices}")

# Obtenha o número de arestas no grafo
num_arestas = G.number_of_edges()
print(f"Número de arestas: {num_arestas}")

# Calcule a assortatividade do grafo (quão bem os nós conectam com outros de grau similar)
assortativity = nx.degree_assortativity_coefficient(G)
print(f"Assortatividade da rede: {assortativity:.4f}")

# Verifique se o grafo é conectado
# graf_connect = nx.is_connected(G)
# print(f"Gráfico conectado: {graf_connect}")

# Calcule o número de componentes conectados no grafo
num_comp_connect = nx.number_connected_components(G)
print(f"Número de componentes conectados: {num_comp_connect}")

# Encontre todos os componentes conectados no grafo
connected_components = list(nx.connected_components(G))

# Calcule o tamanho de cada componente e encontre o tamanho do componente gigante
giant_component_size = max(len(componente) for componente in connected_components)
print(f"Tamanho do componente mais gigante: {giant_component_size}")

# Calcule o coeficiente de clustering médio do grafo
clustering_cof = nx.average_clustering(G)
print(f"Coeficiente de clustering: {clustering_cof}")

# Calcule a média dos graus dos vizinhos de cada nó
degree, avg_neigh_degree = zip(*nx.average_degree_connectivity(G).items())

# Converta as tuplas para listas
degree = list(degree)
avg_neigh_degree = list(avg_neigh_degree)

# Configure o estilo do gráfico
plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Crie um gráfico de dispersão (scatter plot) para mostrar a relação entre o grau dos nós e o grau médio dos vizinhos
sns.regplot(x=degree, y=avg_neigh_degree, ax=ax)

# Configure rótulos do eixo x e y
ax.set_xlabel("Node Degree")
ax.set_ylabel("Average neighbor degree")

# Salve a figura gerada em um arquivo
plt.savefig("degree_assortativity.png", format="png", dpi=400, bbox_inches="tight", transparent=True)

# Mostre o gráfico (se desejado)
plt.show()