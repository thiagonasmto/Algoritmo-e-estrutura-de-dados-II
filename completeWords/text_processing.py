import string
from unidecode import unidecode

def convert_lowercase(text):
    text = text.lower()
    return text

def remove_especial(text):
    text = unidecode(text)
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    return text

def separete_words(text):
    stop_words = ["e", "ou", "mas", "a", "o", "em", "de", "para", "com", "um", ","]
    text = text.split()
    text_without_stop_words = [text for text in text if text.lower() not in stop_words]
    return text_without_stop_words