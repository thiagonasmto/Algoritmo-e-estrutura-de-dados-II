from itertools import product
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
from nxviz import CircosPlot

# Definindo as peças por categoria
categories = {
    "breaks": [
        {"name": "Breakes Wildcore", "category": "Breaks", "speed": 36, "cornering": 23, "power_unit": 33, "reliability": 22, "avg_pitstop_time": 0.59},
        {"name": "Breakes Suspense", "category": "Breaks", "speed": 20, "cornering": 32, "power_unit": 23, "reliability": 21, "avg_pitstop_time": 0.37},
        {"name": "Breakes The Warden", "category": "Breaks", "speed": 26, "cornering": 28, "power_unit": 27, "reliability": 25, "avg_pitstop_time": 0.43},
        {"name": "Breakes Onyx", "category": "Breaks", "speed": 26, "cornering": 23, "power_unit": 25, "reliability": 50, "avg_pitstop_time": 0.49},
        {"name": "Breakes Axiom", "category": "Breaks", "speed": 14, "cornering": 34, "power_unit": 18, "reliability": 15, "avg_pitstop_time": 0.67},
        {"name": "Breakes Crisis SL", "category": "Breaks", "speed": 27, "cornering": 16, "power_unit": 18, "reliability": 19, "avg_pitstop_time": 0.51},
        {"name": "Breakes Essence", "category": "Breaks", "speed": 14, "cornering": 13, "power_unit": 12, "reliability": 25, "avg_pitstop_time": 0.76},
        {"name": "Breakes Starter", "category": "Breaks", "speed": 1, "cornering": 1, "power_unit": 1, "reliability": 1, "avg_pitstop_time": 1.00},
    ],
    "gearbox": [
        {"name": "GearBox Voyage", "category": "GearBox", "speed": 23, "cornering": 28, "power_unit": 22, "reliability": 27, "avg_pitstop_time": 0.00},
        {"name": "GearBox Vector", "category": "GearBox", "speed": 24, "cornering": 38, "power_unit": 22, "reliability": 36, "avg_pitstop_time": 0.55},
        {"name": "GearBox Kick Shift", "category": "GearBox", "speed": 18, "cornering": 19, "power_unit": 29, "reliability": 19, "avg_pitstop_time": 0.45},
        {"name": "GearBox Verdict", "category": "GearBox", "speed": 33, "cornering": 18, "power_unit": 20, "reliability": 30, "avg_pitstop_time": 0.63},
        {"name": "GearBox Spectrum", "category": "GearBox", "speed": 20, "cornering": 25, "power_unit": 21, "reliability": 23, "avg_pitstop_time": 0.53},
        {"name": "GearBox Swiftcharge", "category": "GearBox", "speed": 14, "cornering": 23, "power_unit": 22, "reliability": 16, "avg_pitstop_time": 0.71},
        {"name": "GearBox Switch-R-00", "category": "GearBox", "speed": 12, "cornering": 13, "power_unit": 11, "reliability": 14, "avg_pitstop_time": 0.47},
        {"name": "GearBox Starter", "category": "GearBox", "speed": 1, "cornering": 1, "power_unit": 1, "reliability": 1, "avg_pitstop_time": 1.00},
    ],
    "rear_wing": [
        {"name": "Rear Wing Typhoon", "category": "Rear Wing", "speed": 50, "cornering": 27, "power_unit": 26, "reliability": 23, "avg_pitstop_time": 0.53},
        {"name": "Rear Wing Transcendence", "category": "Rear Wing", "speed": 24, "cornering": 22, "power_unit": 36, "reliability": 37, "avg_pitstop_time": 0.53},
        {"name": "Rear Wing Freeflare", "category": "Rear Wing", "speed": 21, "cornering": 33, "power_unit": 20, "reliability": 22, "avg_pitstop_time": 0.37},
        {"name": "Rear Wing The Patron", "category": "Rear Wing", "speed": 23, "cornering": 21, "power_unit": 19, "reliability": 37, "avg_pitstop_time": 0.61},
        {"name": "Rear Wing The Wasp", "category": "Rear Wing", "speed": 14, "cornering": 24, "power_unit": 23, "reliability": 14, "avg_pitstop_time": 0.69},
        {"name": "Rear Wing The Matador", "category": "Rear Wing", "speed": 19, "cornering": 16, "power_unit": 18, "reliability": 17, "avg_pitstop_time": 0.72},
        {"name": "Rear Wing Phanton", "category": "Rear Wing", "speed": 26, "cornering": 15, "power_unit": 12, "reliability": 11, "avg_pitstop_time": 0.76},
        {"name": "Rear Wing Starter", "category": "Rear Wing", "speed": 1, "cornering": 1, "power_unit": 1, "reliability": 1, "avg_pitstop_time": 1.00},
    ],
    "front_wing": [
        {"name": "Front Wing Virtue", "category": "Front Wing", "speed": 23, "cornering": 50, "power_unit": 27, "reliability": 24, "avg_pitstop_time": 0.49},
        {"name": "Front Wing Thunderclap", "category": "Front Wing", "speed": 35, "cornering": 23, "power_unit": 21, "reliability": 33, "avg_pitstop_time": 0.55},
        {"name": "Front Wing Trailblazer", "category": "Front Wing", "speed": 21, "cornering": 23, "power_unit": 42, "reliability": 20, "avg_pitstop_time": 0.57},
        {"name": "Front Wing Zeno", "category": "Front Wing", "speed": 25, "cornering": 23, "power_unit": 22, "reliability": 26, "avg_pitstop_time": 0.53},
        {"name": "Front Wing The Vagabond", "category": "Front Wing", "speed": 31, "cornering": 20, "power_unit": 23, "reliability": 21, "avg_pitstop_time": 0.35},
        {"name": "Front Wing Feral Punch", "category": "Front Wing", "speed": 13, "cornering": 15, "power_unit": 22, "reliability": 21, "avg_pitstop_time": 0.73},
        {"name": "Front Wing The Scout", "category": "Front Wing", "speed": 13, "cornering": 27, "power_unit": 15, "reliability": 14, "avg_pitstop_time": 0.73},
        {"name": "Front Wing Starter", "category": "Front Wing", "speed": 1, "cornering": 1, "power_unit": 1, "reliability": 1, "avg_pitstop_time": 1.00},
    ],
    "suspension": [
        {"name": "Suspension Sigma", "category": "Suspension", "speed": 32, "cornering": 28, "power_unit": 30, "reliability": 23, "avg_pitstop_time": 0.39},
        {"name": "Suspension Presence", "category": "Suspension", "speed": 23, "cornering": 26, "power_unit": 24, "reliability": 22, "avg_pitstop_time": 0.20},
        {"name": "Suspension Horizon", "category": "Suspension", "speed": 22, "cornering": 36, "power_unit": 24, "reliability": 37, "avg_pitstop_time": 0.53},
        {"name": "Suspension Radiance", "category": "Suspension", "speed": 25, "cornering": 17, "power_unit": 26, "reliability": 19, "avg_pitstop_time": 0.65},
        {"name": "Suspension Icon V3", "category": "Suspension", "speed": 17, "cornering": 13, "power_unit": 16, "reliability": 23, "avg_pitstop_time": 0.54},
        {"name": "Suspension Rodeo", "category": "Suspension", "speed": 23, "cornering": 22, "power_unit": 15, "reliability": 14, "avg_pitstop_time": 0.69},
        {"name": "Suspension The Equator", "category": "Suspension", "speed": 20, "cornering": 19, "power_unit": 18, "reliability": 21, "avg_pitstop_time": 0.61},
        {"name": "Suspension Starter", "category": "Suspension", "speed": 1, "cornering": 1, "power_unit": 1, "reliability": 1, "avg_pitstop_time": 1.00},
    ],
    "engine": [
        {"name": "Engine Cloudroar", "category": "Engine", "speed": 26, "cornering": 24, "power_unit": 50, "reliability": 27, "avg_pitstop_time": 0.55},
        {"name": "Engine Avalanche", "category": "Engine", "speed": 34, "cornering": 22, "power_unit": 25, "reliability": 21, "avg_pitstop_time": 0.35},
        {"name": "Engine The Rover", "category": "Engine", "speed": 27, "cornering": 25, "power_unit": 28, "reliability": 24, "avg_pitstop_time": 0.53},
        {"name": "Engine Twinburst", "category": "Engine", "speed": 16, "cornering": 29, "power_unit": 18, "reliability": 17, "avg_pitstop_time": 0.51},
        {"name": "Engine Enigma", "category": "Engine", "speed": 16, "cornering": 13, "power_unit": 23, "reliability": 25, "avg_pitstop_time": 0.69},
        {"name": "Engine Nova", "category": "Engine", "speed": 31, "cornering": 13, "power_unit": 15, "reliability": 16, "avg_pitstop_time": 0.71},
        {"name": "Engine Brute Force", "category": "Engine", "speed": 21, "cornering": 19, "power_unit": 36, "reliability": 18, "avg_pitstop_time": 0.63},
        {"name": "Engine Starter", "category": "Engine", "speed": 1, "cornering": 1, "power_unit": 1, "reliability": 1, "avg_pitstop_time": 1.00},
    ],
}

data_garrafinhas = [
    {"name": "Tsar", "speed": 0, "cornering": 15, "power_unit": 0, "reliability": 10, "pit_stop": 0, "overtaking": 0, "defending": 10, "race_start": 25, "tyre_management": 0},
    {"name": "Frost", "speed": 0, "cornering": 0, "power_unit": 0, "reliability": 0, "pit_stop": 0, "overtaking": 0, "defending": 0, "race_start": 25, "tyre_management": 10},
    {"name": "Tulip", "speed": 0, "cornering": 0, "power_unit": 0, "reliability": 10, "pit_stop": 20, "overtaking": 0, "defending": 10, "race_start": 0, "tyre_management": 20},
    {"name": "Dragon", "speed": 0, "cornering": 0, "power_unit": 15, "reliability": 0, "pit_stop": 0, "overtaking": 20, "defending": 0, "race_start": 15, "tyre_management": 0},
    {"name": "Kawaii", "speed": 0, "cornering": 20, "power_unit": 0, "reliability": 15, "pit_stop": 0, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Pretzel", "speed": 0, "cornering": 0, "power_unit": 15, "reliability": 10, "pit_stop": 0, "overtaking": 0, "defending": 25, "race_start": 0, "tyre_management": 0},
    {"name": "Vice", "speed": 10, "cornering": 0, "power_unit": 15, "reliability": 0, "pit_stop": 0, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 25},
    {"name": "Schooner", "speed": 0, "cornering": 0, "power_unit": 0, "reliability": 10, "pit_stop": 15, "overtaking": 0, "defending": 10, "race_start": 0, "tyre_management": 25},
    {"name": "Djinn", "speed": 0, "cornering": 15, "power_unit": 0, "reliability": 15, "pit_stop": 0, "overtaking": 0, "defending": 15, "race_start": 0, "tyre_management": 20},
    {"name": "Oud", "speed": 0, "cornering": 10, "power_unit": 0, "reliability": 25, "pit_stop": 15, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Eternal Flame", "speed": 0, "cornering": 0, "power_unit": 0, "reliability": 0, "pit_stop": 25, "overtaking": 0, "defending": 10, "race_start": 15, "tyre_management": 15},
    {"name": "Eagle", "speed": 0, "cornering": 0, "power_unit": 0, "reliability": 15, "pit_stop": 0, "overtaking": 0, "defending": 20, "race_start": 15, "tyre_management": 15},
    {"name": "Iron Force", "speed": 0, "cornering": 0, "power_unit": 20, "reliability": 0, "pit_stop": 0, "overtaking": 0, "defending": 10, "race_start": 10, "tyre_management": 20},
    {"name": "Lumberjack", "speed": 0, "cornering": 0, "power_unit": 0, "reliability": 15, "pit_stop": 0, "overtaking": 15, "defending": 10, "race_start": 25, "tyre_management": 0},
    {"name": "Cranberry", "speed": 0, "cornering": 0, "power_unit": 0, "reliability": 20, "pit_stop": 20, "overtaking": 20, "defending": 0, "race_start": 10, "tyre_management": 0},
    {"name": "Butterfly", "speed": 0, "cornering": 0, "power_unit": 25, "reliability": 5, "pit_stop": 0, "overtaking": 0, "defending": 20, "race_start": 0, "tyre_management": 0},
    {"name": "Tune-in", "speed": 10, "cornering": 15, "power_unit": 0, "reliability": 25, "pit_stop": 0, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Self-Control", "speed": 0, "cornering": 0, "power_unit": 5, "reliability": 0, "pit_stop": 0, "overtaking": 0, "defending": 5, "race_start": 5, "tyre_management": 5},
    {"name": "Warrior", "speed": 10, "cornering": 0, "power_unit": 0, "reliability": 5, "pit_stop": 0, "overtaking": 5, "defending": 5, "race_start": 0, "tyre_management": 0},
    {"name": "Ballast", "speed": 0, "cornering": 10, "power_unit": 0, "reliability": 10, "pit_stop": 0, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Instinct", "speed": 0, "cornering": 0, "power_unit": 15, "reliability": 0, "pit_stop": 0, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 5},
    {"name": "Downforce", "speed": 0, "cornering": 5, "power_unit": 0, "reliability": 15, "pit_stop": 0, "overtaking": 15, "defending": 15, "race_start": 0, "tyre_management": 0},
    {"name": "Hex", "speed": 15, "cornering": 0, "power_unit": 0, "reliability": 5, "pit_stop": 20, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Eggception", "speed": 0, "cornering": 0, "power_unit": 10, "reliability": 15, "pit_stop": 25, "overtaking": 0, "defending": 15, "race_start": 0, "tyre_management": 0},
    {"name": "Rooster", "speed": 0, "cornering": 0, "power_unit": 10, "reliability": 0, "pit_stop": 20, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Cuppa", "speed": 0, "cornering": 20, "power_unit": 0, "reliability": 0, "pit_stop": 10, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Street Sharl", "speed": 15, "cornering": 0, "power_unit": 0, "reliability": 0, "pit_stop": 10, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Herald", "speed": 0, "cornering": 15, "power_unit": 0, "reliability": 0, "pit_stop": 10, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Prince", "speed": 0, "cornering": 20, "power_unit": 0, "reliability": 10, "pit_stop": 0, "overtaking": 10, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Unstoppable", "speed": 15, "cornering": 0, "power_unit": 10, "reliability": 0, "pit_stop": 25, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Dead Fast", "speed": 25, "cornering": 0, "power_unit": 20, "reliability": 0, "pit_stop": 0, "overtaking": 5, "defending": 0, "race_start": 5, "tyre_management": 0},
    {"name": "Gadiator", "speed": 0, "cornering": 0, "power_unit": 10, "reliability": 25, "pit_stop": 0, "overtaking": 25, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Taurus", "speed": 20, "cornering": 0, "power_unit": 25, "reliability": 0, "pit_stop": 5, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Merilion", "speed": 15, "cornering": 25, "power_unit": 0, "reliability": 10, "pit_stop": 0, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Samba", "speed": 5, "cornering": 0, "power_unit": 25, "reliability": 0, "pit_stop": 20, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Caveira", "speed": 25, "cornering": 0, "power_unit": 10, "reliability": 0, "pit_stop": 15, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Fogos", "speed": 20, "cornering": 0, "power_unit": 0, "reliability": 0, "pit_stop": 15, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Movember", "speed": 0, "cornering": 25, "power_unit": 0, "reliability": 15, "pit_stop": 0, "overtaking": 15, "defending": 10, "race_start": 0, "tyre_management": 0},
    {"name": "Palmeira", "speed": 0, "cornering": 0, "power_unit": 0, "reliability": 20, "pit_stop": 0, "overtaking": 20, "defending": 20, "race_start": 0, "tyre_management": 0},
    {"name": "Nazar", "speed": 0, "cornering": 0, "power_unit": 0, "reliability": 0, "pit_stop": 0, "overtaking": 0, "defending": 15, "race_start": 15, "tyre_management": 15},
    {"name": "Aderência", "speed": 0, "cornering": 25, "power_unit": 0, "reliability": 0, "pit_stop": 0, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 15},
    {"name": "Arco-íris", "speed": 20, "cornering": 0, "power_unit": 0, "reliability": 25, "pit_stop": 0, "overtaking": 25, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Eclipse", "speed": 25, "cornering": 0, "power_unit": 0, "reliability": 10, "pit_stop": 15, "overtaking": 0, "defending": 0, "race_start": 0, "tyre_management": 0},
    {"name": "Rena", "speed": 0, "cornering": 10, "power_unit": 0, "reliability": 20, "pit_stop": 20, "overtaking": 0, "defending": 20, "race_start": 0, "tyre_management": 0}
]

# Gerando todas as combinações possíveis de peças
configurations = list(product(*(categories[category] for category in categories)))

# Função para calcular o team score de uma configuração
def calculate_team_score(configuration):
    return sum([
        piece["speed"] + piece["cornering"] + piece["power_unit"] + piece["reliability"] + piece["avg_pitstop_time"]/0.02
        for piece in configuration
    ])

#############################################################
#      IMPRESSÃO DO NÚMERO DE POSSIBILIDADES POR SCORE      #
#############################################################

# Lista para armazenar os team scores
team_scores = []

# Iterando sobre as combinações e calculando os team scores
for combination in configurations:
    team_score = calculate_team_score(combination)
    team_scores.append(team_score)

# Criando o histograma original
plt.hist(team_scores, bins=30, color='green', edgecolor='black', density=False)  # Usando density=False para contar as ocorrências

# Adicionando rótulos e título
plt.xlabel('Team Score')
plt.ylabel('Número de Possibilidades')
plt.title('Número de Possibilidades por Team Score')

# Exibindo o histograma original
plt.show()

#############################################################
#             IMPRESSÃO DO HISTOGRAMA FILTRADO              #
#############################################################

# Lista para armazenar os team scores
team_scores = []

# Iterando sobre as combinações e calculando os team scores
for combination in configurations:
    team_score = calculate_team_score(combination)
    team_scores.append(team_score)

# Filtrando team scores entre 680 e 900
filtered_team_scores = [ts for ts in team_scores if 850 <= ts <= 900]

# Criando o histograma
plt.hist(filtered_team_scores, bins=30, color='green', edgecolor='black', density=False)  # Com density=True para normalizar

# Adicionando rótulos e título
plt.xlabel('Team Score')
plt.ylabel('PDF (Probability Distribution Function)')
plt.title('Histograma de Team Scores (Filtrado de 850 a 900)')
# Limitando o eixo x entre 0 e 100
plt.xlim(850, 900)

# Exibindo o histograma
plt.show()

#############################################################
#                           GRAFO                           #
#############################################################

# Escolha os limites do intervalo
team_score_min = 850
team_score_max = 900

# Encontre as combinações correspondentes a esse intervalo
selected_combinations = [combination for combination in configurations if team_score_min <= calculate_team_score(combination) <= team_score_max]

# Criação do grafo direcionado (DiGraph)
G = nx.DiGraph()

# Adicionando nós e arestas ao grafo
for selected_combination in selected_combinations:
    team_score_example = calculate_team_score(selected_combination)
    team_score_str = f'Team Score {team_score_example:.2f}'
    
    # Adicionando nó do "Team Score" com tamanho e cor fixos
    G.add_node(team_score_str, label=f'Team Score: {team_score_example:.2f}', size=200, color='blue')

    # Adicionando arestas direcionadas das peças para o "Team Score"
    for piece in selected_combination:
        piece_name = piece['name']

        # Adicionando nó da peça, se ainda não existir
        if not G.has_node(piece_name):
            G.add_node(piece_name, label=piece_name)

        # Adicionando aresta direcionada da peça para o "Team Score"
        G.add_edge(piece_name, team_score_str)

# Calculando o tamanho dos nós das peças com base no número de arestas de saída
node_sizes = [G.out_degree(piece_name) * 100 for piece_name in G.nodes()]

# Mapeando os tamanhos dos nós para um mapa de cores (azul a vermelho)
norm = plt.Normalize(min(node_sizes), max(node_sizes))
cmap = plt.get_cmap('coolwarm')
node_colors = [cmap(norm(size)) for size in node_sizes]

# Atribuindo tamanho e cor fixos para os nós "Team Score"
node_sizes_fixed = [200 if 'Team Score' in node else size for node, size in zip(G.nodes(), node_sizes)]
node_colors_fixed = ['blue' if 'Team Score' in node else color for node, color in zip(G.nodes(), node_colors)]

# Desenhando o grafo direcionado com o layout kamada_kawai_layout para espaçamento
pos = nx.kamada_kawai_layout(G)
labels = nx.get_edge_attributes(G, 'label')
nx.draw(G, pos, with_labels=True, labels=nx.get_node_attributes(G, 'label'), font_size=8, node_size=node_sizes_fixed, node_color=node_colors_fixed, font_color='black', font_weight='bold', edge_color='gray', connectionstyle="arc3,rad=0.1", arrowsize=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Adicionando rótulo de título
plt.title('Grafo Direcionado de Compatibilidade de Combinações com Tamanhos Proporcionais e Cores Variadas')

# Exibindo o grafo direcionado
plt.show()

#############################################################
#                     IMPRESSÃO DA PDF                      #
#############################################################

# Imprimindo os valores do Out Degree
for node in G.nodes:
    out_degree = G.out_degree(node)
    print(f"Node: {node}, Out Degree: {out_degree}")

# Criando o grau de saída para cada nó (vértice)
out_degrees_pieces = [G.out_degree(node) for node in G.nodes if "Team Score" not in node]

# Verificando se há dados antes de plotar
if out_degrees_pieces:
    # Criando o gráfico de PDF usando Seaborn
    plt.figure(figsize=(8, 6))
    sns.kdeplot(out_degrees_pieces, fill=True, color='skyblue')
    plt.title('PDF do Out Degree dos Nós das Peças')
    plt.xlabel('Out Degree')
    plt.ylabel('PDF (Probability Density Function)')
    plt.xlim(0, 60)  # Limitando o eixo x entre 0 e 60
    plt.show()
else:
    print("Não há dados para plotar.")

#############################################################
#                    PESQUISA DE SCORE                      #
#############################################################

def choose_combinations(configurations, num_choices, score_range=None):
    # Calcula os team scores para todas as combinações
    team_scores = [calculate_team_score(combination) for combination in configurations]
    
    # Filtra as combinações com base no score_range, se fornecido
    if score_range:
        min_score, max_score = score_range
        filtered_indices = [i for i, score in enumerate(team_scores) if min_score <= score <= max_score]
    else:
        filtered_indices = range(len(configurations))
    
    # Índices ordenados pelos scores (do maior para o menor)
    sorted_indices = sorted(filtered_indices, key=lambda i: team_scores[i], reverse=True)
    
    # Escolhe as primeiras 'num_choices' combinações
    selected_combinations = [configurations[i] for i in sorted_indices[:num_choices]]
    
    # Retorna as combinações escolhidas e seus scores correspondentes
    chosen_scores = [calculate_team_score(combination) for combination in selected_combinations]
    
    return selected_combinations, chosen_scores

# Escolhe as 5 melhores combinações dentro do intervalo de scores de 850 a 900
num_choices = 5
score_range = (400, 700)
chosen_combinations, chosen_scores = choose_combinations(configurations, num_choices, score_range)

# Imprime as combinações escolhidas e seus scores
for combination, score in zip(chosen_combinations, chosen_scores):
    print(f"Combinação: {combination}, Score: {score}")

#############################################################
#                     GRAFO BIPARTIDO                       #
#############################################################

G = nx.Graph()

# Separe os nós em dois grupos: 'Garrafinhas' e 'Propriedades'
garrafinhas = [garrafinha["name"] for garrafinha in data_garrafinhas]
propriedades = [
    "speed", "cornering", "power_unit", "reliability", "pit_stop", "overtaking", "defending", "race_start", "tyre_management"
]

G.add_nodes_from(garrafinhas, bipartite=0)
G.add_nodes_from(propriedades, bipartite=1)

# Adicione arestas do grupo de propriedades para o grupo de garrafinhas
for garrafinha in garrafinhas:
    for propriedade in propriedades:
        peso = data_garrafinhas[garrafinhas.index(garrafinha)][propriedade]
        if peso > 0:
            G.add_edge(garrafinha, propriedade, weight=peso)  # Adicione o peso como atributo

# Calcular o Out Degree de cada nó no grupo de propriedades
out_degree = {propriedade: 0 for propriedade in propriedades}
for propriedade in propriedades:
    for garrafinha in garrafinhas:
        if G.has_edge(garrafinha, propriedade):
            peso = G[garrafinha][propriedade]["weight"]
            out_degree[propriedade] += peso

# Calcular o tamanho dos vértices das Propriedades proporcional ao Out Degree
propriedade_sizes = [out_degree[propriedade] for propriedade in propriedades]

# Desenhar o grafo
pos = nx.bipartite_layout(G, garrafinhas)
nx.draw_networkx_nodes(G, pos, nodelist=garrafinhas, node_color='b', node_size=500)
nx.draw_networkx_nodes(G, pos, nodelist=propriedades, node_color='r', node_size=propriedade_sizes)
labels = {propriedade: f'{propriedade}: OutDegree = {out_degree[propriedade]}' for propriedade in propriedades}
nx.draw_networkx_labels(G, pos, labels={node: node for node in garrafinhas}, font_size=8)  # Adicione isso para os nós das garrafinhas
nx.draw_networkx_labels(G, pos, labels=labels, font_size=8)
edges = G.edges()
edge_labels = {(u, v): G[u][v]['weight'] for u, v in edges}  # Rótulos das setas
nx.draw_networkx_edges(G, pos, edgelist=edges, width=1.0, edge_color='grey')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.5, font_size=8)
plt.axis('off')
plt.show()

#############################################################
#                      GRAFO CIRCULAR                       #
#############################################################

G = nx.Graph()

# Separe os nós em dois grupos: 'Garrafinhas' e 'Propriedades'
garrafinhas = [garrafinha["name"] for garrafinha in data_garrafinhas]
propriedades = [
    "speed", "cornering", "power_unit", "reliability", "pit_stop", "overtaking", "defending", "race_start", "tyre_management"
]

G.add_nodes_from(garrafinhas, bipartite=0)
G.add_nodes_from(propriedades, bipartite=1)

# Adicione arestas do grupo de propriedades para o grupo de garrafinhas
for garrafinha in garrafinhas:
    for propriedade in propriedades:
        peso = data_garrafinhas[garrafinhas.index(garrafinha)][propriedade]
        if peso > 0:
            G.add_edge(garrafinha, propriedade, weight=peso)  # Adicione o peso como atributo

# Calcular o Out Degree de cada nó no grupo de propriedades
out_degree = {propriedade: 0 for propriedade in propriedades}
for propriedade in propriedades:
    for garrafinha in garrafinhas:
        if G.has_edge(garrafinha, propriedade):
            peso = G[garrafinha][propriedade]["weight"]
            out_degree[propriedade] += peso

# Calcular o tamanho dos vértices das Propriedades proporcional ao Out Degree
propriedade_sizes = [out_degree[propriedade] for propriedade in propriedades]

# Desenhar o grafo em um layout circular
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, nodelist=garrafinhas, node_color='b', node_size=500)
nx.draw_networkx_nodes(G, pos, nodelist=propriedades, node_color='r', node_size=propriedade_sizes)
labels = {propriedade: f'{propriedade}: OutDegree = {out_degree[propriedade]}' for propriedade in propriedades}
nx.draw_networkx_labels(G, pos, labels={node: node for node in garrafinhas}, font_size=8)  # Adicione isso para os nós das garrafinhas
nx.draw_networkx_labels(G, pos, labels=labels, font_size=8)
edges = G.edges()
edge_labels = {(u, v): G[u][v]['weight'] for u, v in edges}  # Rótulos das setas
nx.draw_networkx_edges(G, pos, edgelist=edges, width=1.0, edge_color='grey')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.5, font_size=8)
plt.axis('off')
plt.show()