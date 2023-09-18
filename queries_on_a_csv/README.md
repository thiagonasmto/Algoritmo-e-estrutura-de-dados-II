## **Projeto Guiado - Construindo Consultas Rápidas em um CSV** 📊

Olá! Bem-vindo ao meu repositório pessoal. Aqui, você encontrará os resultados do curso "Data Engineer" oferecido pela plataforma Dataquest. Um dos destaques desse curso foi o projeto guiado, intitulado "Guided Project: Building Fast Queries on a CSV." Este projeto me auxiliou no aprimoramento das minhas habilidades em manipulação eficiente de dados tabulares com Python.

### Descrição do Projeto:

**Título:** Guided Project: Building Fast Queries on a CSV 💻

**Objetivo:** O objetivo deste projeto é desenvolver uma classe Python chamada `Inventory` que permita realizar consultas rápidas em um arquivo CSV contendo informações sobre laptops. A classe implementa diversos métodos para realizar consultas eficazes, como busca por ID de laptop, verificação de preços promocionais e pesquisa de intervalo de preços.

### **Visualização de Métodos Desenvolvidos:**

```python
# Pesquisa por intervalo de preços.
def range_search(self, target_min_price, target_max_price):
        laptops_in_range = []
        start_index = self.find_laptop_with_price(target_min_price)
        
        if start_index == -1:
            return laptops_in_range  # Nenhum laptop encontrado no intervalo
        
        end_index = self.find_first_laptop_more_expensive(target_max_price)
        
        if end_index == -1:
            end_index = len(self.rows_by_price) - 1  # Defina o final como o último laptop disponível
        
        for index in range(start_index, end_index + 1):
            laptops_in range.append(self.rows_by_price[index])
        
        return laptops_in_range
```
```python
 # Filtra o laptop mais barato com uma determinada RAM e capacidade de HD
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

### Principais Características do Código:

1. **Leitura e Processamento do CSV:** A classe `Inventory` começa carregando um arquivo CSV com informações sobre laptops. Ela extrai o cabeçalho e as linhas do arquivo, converte os preços em números inteiros e cria estruturas de dados para acesso rápido, como um mapeamento de ID para linha e um conjunto de preços únicos.

2. **Consultas Eficientes:** A classe `Inventory` fornece métodos para consultas eficientes, como `get_laptop_from_id` para buscar laptops por ID, `check_promotion_dollars` para verificar preços de promoção válidos e `range_search` para encontrar laptops dentro de um intervalo de preços especificado.

3. **Ordenação de Dados:** Os laptops são ordenados por preço, facilitando consultas que envolvem a classificação por preço.

4. **Método de Filtragem:** O método `cheapest_filter` permite filtrar laptops pelo tamanho da RAM e capacidade de HD, retornando o laptop mais barato que atende aos critérios especificados.

Fique à vontade para explorar o código-fonte e os resultados deste projeto. Se tiver alguma dúvida ou precisar de mais informações, não hesite em entrar em contato pelo e-mail thiagonasmento20@gmail.com. Estou à disposição para ajudar! 📧
