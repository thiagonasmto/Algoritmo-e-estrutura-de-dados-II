# Importa a biblioteca 'string' para manipular caracteres especiais e a biblioteca 'unidecode' para remover acentos.
import string
from unidecode import unidecode

# Função para converter o texto em minúsculas.
def convert_lowercase(text):
    # Converte o texto para letras minúsculas.
    text = text.lower()
    return text

# Função para remover caracteres especiais e acentos do texto.
def remove_especial(text):
    # Remove acentos do texto usando a biblioteca 'unidecode'.
    text = unidecode(text)
    
    # Cria um tradutor para remover caracteres de pontuação usando a tabela de tradução 'string.punctuation'.
    translator = str.maketrans('', '', string.punctuation)
    
    # Remove os caracteres de pontuação do texto.
    text = text.translate(translator)
    return text

# Função para separar palavras do texto e remover palavras de parada.
def separete_words(text):
    # Lista de palavras de parada (stop words) a serem removidas do texto.
    stop_words = ["e", "ou", "mas", "a", "o", "em", "de", "para", "com", "um", ","]
    
    # Divide o texto em palavras individuais.
    text = text.split()
    
    # Filtra as palavras do texto, removendo aquelas que estão na lista de palavras de parada.
    text_without_stop_words = [text for text in text if text.lower() not in stop_words]
    return text_without_stop_words
