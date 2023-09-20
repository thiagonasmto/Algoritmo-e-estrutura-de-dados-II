## Projeto Guiado - Construindo Consultas Rápidas em um CSV 📊

Bem-vindo ao meu repositório pessoal! Aqui, você encontrará os resultados do curso "Data Engineer" oferecido pela plataforma Dataquest. Um dos destaques desse curso foi o projeto guiado, intitulado "Guided Project: Building Fast Queries on a CSV." Este projeto me auxiliou no aprimoramento das minhas habilidades em manipulação eficiente de dados tabulares com Python.

### Descrição do Projeto

**Título:** Building Fast Queries on a CSV 💻

O objetivo deste projeto é desenvolver uma classe Python chamada `Inventory` que permita realizar consultas rápidas em um arquivo CSV contendo informações sobre laptops. A classe implementa diversos métodos para realizar consultas eficazes, como busca por ID de laptop, verificação de preços promocionais e pesquisa de intervalo de preços.

### Análise de Complexidade dos Métodos

Aqui, faremos uma análise de complexidade dos principais métodos desenvolvidos na classe `Inventory` para realizar consultas eficientes em um arquivo CSV contendo informações sobre laptops; você também pode assitir ao vídeo explicativo [aqui!](https://www.loom.com/share/74c4c8783a8241b3a8a03823c4f94157)

#### Método `range_search(target_min_price, target_max_price)`

```python
def range_search(self, target_min_price, target_max_price):
    laptops_in_range = []
    start_index = self.find_first_laptop_cheaper(target_min_price)
    
    if start_index == -1:
        return laptops_in_range  # Nenhum laptop encontrado no intervalo
    
    end_index = self.find_first_laptop_more_expensive(target_max_price)
    
    if end_index == -1:
        end_index = len(self.rows_by_price) - 1  # Defina o final como o último laptop disponível
    
    for index in range(start_index, end_index + 1):
        laptops_in_range.append(self.rows_by_price[index])
    
    return laptops_in_range
```

A complexidade deste método depende principalmente das chamadas aos métodos `find_first_laptop_cheaper` e `find_first_laptop_more_expensive`. Vamos analisar cada um deles:

- `find_first_laptop_cheaper(target_min_price)`:

  - O método faz uma pesquisa binária (busca binária) no vetor `self.rows_by_price` para encontrar o índice do primeiro laptop cujo preço é menor ou igual a `target_min_price`.
  - A complexidade da busca binária é O(log n), onde "n" é o número de laptops.
  - Portanto, a complexidade deste método é dominada pela busca binária e é O(log n).

- `find_first_laptop_more_expensive(target_max_price)`:

  - Este método é semelhante ao `find_first_laptop_cheaper`, mas busca o índice do primeiro laptop cujo preço é maior do que `target_max_price`.
  - Novamente, a complexidade é O(log n), onde "n" é o número de laptops.

- A iteração subsequente que cria a lista `laptops_in_range` envolve um loop que itera sobre os índices do vetor de laptops de `start_index` a `end_index`. O número de laptops dentro do intervalo de preços é proporcional a `end_index - start_index + 1`.
- Portanto, a complexidade deste loop é O(end_index - start_index), que é no máximo O(n), onde "n" é o número total de laptops.

Portanto, a complexidade geral do método `range_search` é dominada pelas buscas binárias e é O(log n) no caso médio, O(n) no pior, onde "n" é o número total de laptops, e O(1) no melhor caso.

#### Método `cheapest_filter(size_ram, size_hd)`

```python
def cheapest_filter(self, size_ram, size_hd):
    for laptop in self.rows_by_price:
        ram_str = laptop[7]  # O índice 7 representa a coluna 'Ram' no CSV
        hd_str = laptop[8]  # O índice 8 representa a coluna 'Memory' no CSV

        # Função auxiliar para extrair a quantidade de RAM da string.
        def parse_ram(ram_string):
            try:
                return int(ram_string.split('GB')[0])
            except ValueError:
                return 0

        # Função auxiliar para extrair a quantidade de HD da string.
        def parse_hd(hd_string):
            try:
                if 'GB' in hd_string:
                    return int(hd_string.split('GB')[0])
                elif 'TB' in hd_string:
                    return int(hd_string.split('TB')[0])*1024
                else:
                    return 0
            except ValueError:
                return 0

        ram = parse_ram(ram_str)
        hd = parse_hd(hd_str)
        
        if ram == size_ram and hd == size_hd:
            return laptop
```

Neste método, há um loop que itera sobre cada laptop no vetor `self.rows_by_price`. Dentro do loop, há duas operações principais:

1. As funções `parse_ram` e `parse_hd` são chamadas para extrair a quantidade de RAM e capacidade de HD do laptop. Essas funções envolvem operações de divisão de strings e conversões para números inteiros, mas seu tempo de execução é limitado e não depende do número total de laptops. Portanto, a complexidade dessas operações é O(1) para cada laptop.

2. A comparação `if ram == size_ram and hd == size_hd` verifica se o laptop atende aos critérios especificados. Essa comparação é executada uma vez para cada laptop.
   - Portanto, a complexidade deste método é O(n), onde "n" é o número total de laptops.

Em resumo, a complexidade geral do método `cheapest_filter` é linear em relação ao número de laptops, que é O(n) na pior hipótese, O(1) na melhor e O(n/2) no caso médio.

### Principais Características do Código

1. **Leitura e Processamento do CSV:** A classe `Inventory` começa carregando um arquivo CSV com informações sobre laptops. Ela extrai o cabeçalho e as linhas do arquivo, converte os preços em números inteiros e cria estruturas de dados para acesso rápido, como um mapeamento de ID para linha e um conjunto de preços únicos.

2. **Consultas Eficientes:** A classe `Inventory` fornece métodos para consultas eficientes, como `get_laptop_from_id` para buscar laptops por ID, `check_promotion_dollars` para verificar preços de promoção válidos e `range_search` para encontrar laptops dentro de um intervalo de preços especificado.

3. **Ordenação de Dados:** Os laptops são ordenados por preço, facilitando consultas que envolvem a classificação por preço.

4. **Método de Filtragem:** O método `cheapest_filter` permite filtrar laptops pelo tamanho da RAM e capacidade de HD, retornando o laptop mais barato que atende aos critérios especificados.

Sinta-se à vontade para explorar o código-fonte e os resultados deste projeto. Se tiver alguma dúvida ou precisar de mais informações, não hesite em entrar em contato pelo e-mail thiagonasmento20@gmail.com. Estou à disposição para ajudar! 📧
