import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

'''
Leitura do arquivo de arestas - conexões entre pessoas no Facebook
This dataset consists of 'circles' (or 'friends lists') from Facebook. 
Facebook data was collected from survey participants using Facebook app. 
The dataset includes node features (profiles), circles, and ego networks.
'''
# G = nx.read_edgelist('./small_worlds/data/facebook_combined.txt', nodetype=int)

'''
Leitura do arquivo de arestas - conexões de computadores
A sequence of snapshots of the Gnutella peer-to-peer file sharing network from August 2002. 
There are total of 9 snapshots of Gnutella network collected in August 2002. 
Nodes represent hosts in the Gnutella network topology and edges represent connections between the Gnutella hosts.
'''
#G = nx.read_edgelist('./small_worlds/data/p2p-Gnutella04.txt', nodetype=int)

'''
Leitura do arquivo de arestas - conexões de produtos da Amazon
Network was collected by crawling Amazon website. It is based on Customers Who Bought This Item Also Bought feature of the Amazon website. 
If a product i is frequently co-purchased with product j, the graph contains a directed edge from i to j.
'''
#G = nx.read_edgelist('./small_worlds/data/Amazon0302.txt', nodetype=int)

'''
Leitura do arquivo de arestas - Enron email network
Enron email communication network covers all the email communication within a dataset of around half million emails. 
This data was originally made public, and posted to the web, by the Federal Energy Regulatory Commission during its investigation. 
Nodes of the network are email addresses and if an address i sent at least one email to address j, the graph contains an undirected edge from i to j. 
Note that non-Enron email addresses act as sinks and sources in the network as we only observe their communication with the Enron email addresses.
'''
#G = nx.read_edgelist('./small_worlds/data/Email-Enron.txt', nodetype=int)

'''
Leitura do arquivo de arestas - Pennsylvania road network
This is a road network of Pennsylvania. 
Intersections and endpoints are represented by nodes, and the roads connecting these intersections or endpoints are represented by undirected edges.
'''
G = nx.read_edgelist('./small_worlds/data/roadNet-PA.txt', nodetype=int)

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