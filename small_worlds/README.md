# Análise de Rede Social

Este código realiza uma análise de uma rede social representada por um arquivo de arestas. Ele calcula várias métricas e produz visualizações relacionadas às propriedades do grafo.

## Executando o Código

Para executar o código:

1. Certifique-se de ter o Python instalado.
2. Instale as bibliotecas necessárias executando `pip install networkx matplotlib seaborn`.
3. Coloque o arquivo de arestas (`facebook_combined.txt`) no diretório `./small_worlds/data/`.

Execute o script `analyze_social_network.py`:

```bash
python analyze_social_network.py
```

## Resultados

O código fornecerá as seguintes informações sobre a rede social:

Claro, aqui está a tabela com o cabeçalho centralizado:

|          Rede                 | Número de Vértices | Número de Arestas  | Assortatividade | Componentes Conectados | Tamanho Componente Mais Gigante | Coeficiente de Clustering    |
|:-----------------------------:|:------------------:|:------------------:|:---------------:|:----------------------:|:-------------------------------:|:----------------------------:|
| Facebook Social Circles       |      4039          |       88234        |      0.0636     |          1             |              4039               |     0.6055467186200876       |
| Gnutella Peer-to-Peer Network |      10876         |       39994        |     -0.0132     |          1             |             10876               |     0.0062175327714660625    |
| Amazon Product Co-Purchasing  |      262111        |       899792       |     -0.0025     |          1             |            262111               |     0.419780014607673        |
| Enron Email Network           |      36692         |      183831        |     -0.1108     |         1065           |             33696               |     0.49698255959950266      |
| Pennsylvania Road Network     |      1088092       |      1541898       |     0.1227      |         206            |            1087562              |     0.04647676048519474      |


Agora o cabeçalho da tabela está centralizado. Se precisar de mais alguma modificação, por favor, me avise.

## Gráfico de Grau vs. Grau Médio dos Vizinhos

![Grau vs. Grau Médio dos Vizinhos](assets/degree_avg_neigbhour_degree_Social circles_Facebook.png)

### Análise do Gráfico

#### Assortatividade:
O fato de que os nós com grau 0 possuem um average neighbor degree próximo a 500 e os nós com grau 800 possuem um average neighbor degree abaixo de 50 sugere uma forte assortatividade positiva na rede. Isso significa que os nós com graus semelhantes tendem a se conectar uns com os outros, o que é consistente com a ideia de que usuários do Facebook têm uma tendência a se conectar com outros usuários que têm um número semelhante de conexões (amigos).

#### Hubs e Isolados:
Os nós com grau 0 representam provavelmente os usuários "isolados" que têm poucas ou nenhuma conexão, mas seus vizinhos (caso tenham algum) têm um número significativamente maior de conexões. Por outro lado, os nós com grau 800 são "hubs" com muitas conexões, mas seus vizinhos têm um número relativamente menor de conexões.

#### Variação no Grau:
Para valores de grau entre 0 e 200, a variação no average neighbor degree está entre 50 e 200. Isso sugere que, em geral, usuários com um número moderado de conexões têm vizinhos com um número razoável de conexões, mas a diferença entre o grau do nó e o grau médio dos vizinhos pode ser significativa.

#### Conectividade em Subgrupos:
O gráfico pode indicar a presença de subgrupos na rede, onde usuários com números semelhantes de conexões tendem a formar clusters distintos. Esses subgrupos podem ser comunidades de interesse ou grupos de amigos.

#### Variação no Comportamento de Usuários:
A ampla variação no average neighbor degree sugere que os usuários do Facebook têm diferentes comportamentos de conexão. Alguns podem se concentrar em estabelecer conexões com muitos outros usuários, enquanto outros podem preferir um círculo de amigos mais restrito.

## Arquivos Gerados

O código gera uma imagem (`degree_assortativity.png`) representando a análise do grafo.

---

Este README inclui a análise do gráfico de grau vs. grau médio dos vizinhos, destacando as descobertas e insights com base nas observações do gráfico. Certifique-se de adicionar a imagem `degree_avg_neighbour_degree.png` à pasta `assets` para que a imagem seja exibida corretamente no seu README.
