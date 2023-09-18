**Repositório: Projeto Guiado - Construindo Consultas Rápidas em um CSV**

Este repositório é parte integrante do curso "Data Engineer" oferecido na plataforma Dataquest. O projeto guiado, intitulado "Guided Project: Building Fast Queries on a CSV," é um componente fundamental deste curso que visa aprimorar suas habilidades na manipulação eficiente de dados tabulares em Python. Abaixo, fornecemos uma visão geral detalhada deste projeto e seu código-fonte associado.

### Descrição do Projeto:

**Título:** Guided Project: Building Fast Queries on a CSV

**Objetivo:** Este projeto tem como objetivo construir uma classe Python chamada `Inventory` que permite a realização de consultas rápidas em um arquivo CSV contendo informações sobre laptops. A classe implementa vários métodos para realizar consultas eficientes, como a busca por ID de laptop, verificação de preços de promoção e pesquisa por intervalo de preços. O projeto visa melhorar suas habilidades em estruturas de dados, algoritmos de pesquisa e manipulação de dados tabulares.

**Código de Exemplo:**
```python
# Exemplo de uso:
inventory = Inventory('laptops.csv')
print(inventory.cheapest_filter(8, 256))
min_price = 400  # Defina o preço mínimo desejado
max_price = 600  # Defina o preço máximo desejado
laptops_in_range = inventory.range_search(min_price, max_price)

if laptops_in_range:
    for laptop in laptops_in_range:
        print(f"ID: {laptop[0]}, Name: {laptop[1]}, RAM: {laptop[7]}, HD: {laptop[8]}, Price: {laptop[-1]}")
else:
    print("Nenhum laptop encontrado dentro do intervalo de preços especificado.")
```

### Principais Características do Código:

1. **Leitura e Processamento do CSV:** A classe `Inventory` inicia carregando um arquivo CSV contendo informações sobre laptops. Ele extrai o cabeçalho e as linhas do arquivo, converte os preços para números inteiros e cria estruturas de dados para acesso rápido, como um mapeamento de ID para linha e um conjunto de preços únicos.

2. **Consultas Eficientes:** A classe `Inventory` fornece métodos para consultas eficientes, como `get_laptop_from_id` para buscar laptops por ID, `check_promotion_dollars` para verificar preços de promoção válidos e `range_search` para encontrar laptops dentro de um intervalo de preços especificado.

3. **Ordenação de Dados:** Os laptops são ordenados por preço, facilitando consultas que envolvem a classificação por preço.

4. **Método de Filtragem:** O método `cheapest_filter` permite filtrar laptops pelo tamanho da RAM e da capacidade de HD, retornando o laptop mais barato que atende aos critérios especificados.

### Como Usar o Projeto:

Para utilizar este projeto, siga estas etapas:

1. Clone ou faça o download deste repositório em sua máquina local.
2. Certifique-se de ter um arquivo CSV contendo informações sobre laptops (semelhante ao fornecido no exemplo).
3. Importe a classe `Inventory` e crie uma instância, passando o caminho para o arquivo CSV como argumento.
4. Utilize os métodos da classe `Inventory` para realizar consultas eficientes em seus dados.

Este projeto é uma oportunidade valiosa para aprimorar suas habilidades em manipulação de dados e desenvolvimento Python, especialmente se você estiver interessado em se tornar um engenheiro de dados. Aproveite a oportunidade para explorar e expandir esse código e aplicar os conceitos aprendidos no curso "Data Engineer" da plataforma Dataquest.
