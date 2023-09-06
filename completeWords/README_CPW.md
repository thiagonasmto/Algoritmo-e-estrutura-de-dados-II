## Desafio de Autocompletar Palavras com Árvore AVL

**Introdução:**

A atividade proposta envolve a criação de um sistema de autocompletar palavras utilizando uma estrutura de dados conhecida como Árvore AVL. O objetivo principal é desenvolver uma aplicação capaz de sugerir palavras completas com base em um prefixo fornecido, tornando-se uma ferramenta valiosa para diversos cenários, como corretores ortográficos, mecanismos de busca e aplicativos de digitação.

**Objetivos Principais:**

1. **Implementar uma Árvore AVL:** O cerne deste desafio é a criação de uma Árvore AVL (Árvore Binária de Busca Balanceada), uma estrutura de dados eficiente para armazenar e recuperar palavras de forma rápida e ordenada.

2. **Carregar um Corpus:** Para alimentar o sistema de autocompletar, será necessário carregar um corpus, que pode ser um conjunto de textos, livros, artigos, tweets ou qualquer outra fonte de texto. Este corpus servirá como base para extrair todas as palavras únicas que serão inseridas na Árvore AVL.

3. **Extrair Palavras Únicas:** Após carregar o corpus, o próximo passo é extrair todas as palavras únicas contidas nele. Isso requer a capacidade de processar o texto, dividindo-o em palavras e removendo duplicatas.

4. **Inserir Palavras na Árvore AVL:** As palavras únicas extraídas serão inseridas na Árvore AVL. A estrutura da árvore deve ser mantida balanceada para garantir uma busca eficiente.

5. **Implementar a Função de Autocompletar:** O coração do sistema é a função que recebe um prefixo (a parte inicial de uma palavra) e retorna uma lista de possíveis palavras completas que podem ser encontradas na Árvore AVL. Isso envolve uma busca na árvore a partir do prefixo fornecido e a coleta de todas as palavras que correspondem ao prefixo.

**Descrição:**

A atividade de autocompletar palavras usando uma Árvore AVL é uma demonstração fascinante da aplicação de estruturas de dados e algoritmos em problemas do mundo real. A capacidade de sugerir palavras completas com base em um prefixo é fundamental em muitas aplicações, desde assistentes de digitação até mecanismos de busca sofisticados.

Ao concluir este desafio, você terá adquirido conhecimentos valiosos sobre estruturas de dados, algoritmos de busca e manipulação de texto. Além disso, terá construído uma ferramenta útil que pode ser usada em diversos contextos.

Portanto, prepare-se para explorar os conceitos de árvores AVL e processamento de texto enquanto enfrenta este desafio empolgante de autocompletar palavras.

**Solução:**

Neste projeto, foi implementado um sistema de autocompletar palavras usando uma Árvore AVL. Aqui estão os principais arquivos relacionados ao projeto:

1. [**main.py**](./main.py): Este é o arquivo principal que contém a lógica central do sistema de autocompletar palavras. Você pode explorar e entender como a aplicação funciona a partir deste arquivo.

2. [**text_processing.py**](./text_processing.py): Este arquivo contém funções e métodos relacionados ao processamento de texto. Ele desempenha um papel importante na extração de palavras únicas do corpus.

3. [**AVL.py**](./AVL.py): Aqui, você encontrará a implementação da Árvore AVL, que é a estrutura de dados fundamental para armazenar e recuperar palavras de forma eficiente.

4. [**AVL_BST_Performance_Test.py**](./AVL_BST_Performance_Test.py): Este arquivo contém testes de desempenho que comparam a eficiência da Árvore AVL com a Árvore Binária de Busca padrão (BST). É útil para entender como a Árvore AVL melhora a velocidade de pesquisa.

Sinta-se à vontade para explorar esses links para obter uma visão mais aprofundada do projeto e do código-fonte. Se tiver alguma dúvida ou sugestão, não hesite em entrar em contato conosco. Estamos animados para compartilhar este projeto com você!
