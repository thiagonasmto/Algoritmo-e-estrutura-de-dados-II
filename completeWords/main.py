from AVL import AVLTree

# Crie uma instância da classe AVLTree
avl_tree = AVLTree()

# Adicione algumas palavras à Árvore AVL
palavras = ["O sol brilha durante o dia enquanto a lua brilha durante a noite.",
            "O gato caça o rato, enquanto o cachorro caça o gato.", 
            "As frutas são saudáveis. Adoro comer maçãs, bananas e uvas.", 
            "Programar em Python, Java e C++ é divertido.", 
            "Gosto de café, chá e suco. Mas evito refrigerante.", 
            "Ela estuda matemática, física e química.", 
            "Os planetas do sistema solar são Mercúrio, Vênus, Terra, Marte, Júpiter,Saturno, Urano e Netuno.",
            "Nadar, correr e pular são atividades físicas.",
            "As estações do ano são primavera, verão, outono e inverno.",
            "As cores do arco-íris são vermelho, laranja, amarelo, verde, azul, anil evioleta."
           ]
for palavra in palavras:
    avl_tree.add(palavra)

# Realize a impressão da Árvore AVL em ordem
avl_tree.print_in_order()

# Realize a busca de palavras com prefixo "app"
prefixo = "s"
palavras_com_prefixo = avl_tree.search_words_with_prefix(prefixo)

print("Palavras com prefixo '{}':".format(prefixo))

for palavra in palavras_com_prefixo:
    print(palavra)
