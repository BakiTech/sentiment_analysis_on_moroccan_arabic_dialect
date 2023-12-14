import nltk

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_custom_arabic_stopwords(text):
    # Liste des stopwords en arabe
    arabic_stopwords = set(stopwords.words('arabic'))
    # Mots à exclure
    custom_stopwords = ['أقبل', 'إيه', 'بؤسا', 'بئس', 'لست', 'لستم', 'لستما', 'لستن', 'لسن', 'لسنا',
                        'ليس', 'ليسا', 'ليست', 'ليستا', 'ليسوا', 'نعم', 'لا', 'أجل']

    # Suppression des mots spécifiques des stopwords
    arabic_stopwords = arabic_stopwords - set(custom_stopwords)
    
    custom_stopwords_to_add = ['اين','عد', 'بعد', 'لأن', 'مع', 'او', 'مني', 'بين', 'لي', 'لاكن',
                                'انه','اما','شي','بل', 'كل', 'ما', 'فينهو', 'الكل', 'لو', 'باش', 'بان', 'ودوك', 'حتى',
                                'او', 'راه', 'وا',  'فهو', 'لي', 'أما', 'عنه', 'يا', 'اننا',
                                'لينا', 'ثم', 'مشي', 'مش','الشئ', 'الى','انا','الى','الل','ان','وان','وان','الان']

    # Ajout des mots spécifiques à l'ensemble des stopwords
    arabic_stopwords.update(custom_stopwords_to_add)
    
    # Tokenisation
    words = word_tokenize(text)

    # Suppression des stopwords
    filtered_words = [word for word in words if word.lower() not in arabic_stopwords]

    # Reconstitution du texte
    filtered_text = ' '.join(filtered_words)

    return filtered_text
    #supprimer les mots d'un seul caractere
def remove_single_char_words(text):
    # Utilise une expression régulière pour supprimer les mots d'un seul caractère
    pattern = re.compile(r'\b\w\b', re.UNICODE)
    
    # Remplace les occurrences par une chaîne vide
    cleaned_text = pattern.sub('', text)
    
    return cleaned_text
#remove hhhhh
def remove_ha_sequences(text):
    # Utilise une expression régulière pour trouver toutes les séquences de la lettre "ه"
    pattern = re.compile(r'(هه)+', re.UNICODE)
    # Remplace toutes les occurrences par une chaîne vide
    cleaned_text = pattern.sub('', text)
    
    return cleaned_text
#remove les article definit
def remove_definite_article(word):
    # Function to remove Arabic definite article "ال"
    word = re.sub('^ال', '', word)
    word = re.sub('^وال', '', word)
    word = re.sub('^لل', '', word)
    return word
import re
import string
import numpy as np
def wordopt(text):
    text = re.sub('\[.*?\]', '', text)
    
    text = re.sub('[^a-zA-Z0-9\s\u0600-\u06FF]', ' ', text)
    
    text = re.sub('https?://\S+|www\.\S+', '', text)
    
    text = re.sub('<.*?>+', '', text)
    
    arabic_punctuation = 'ء،؛؟«»'
    text = re.sub('[%s%s]' % (re.escape(string.punctuation), re.escape(arabic_punctuation)), ' ', text)
    
    text = re.sub('\n', '', text)
    
    text = re.sub('أ', 'ا', text)
    
    text = re.sub('\w*\d\w*', '', text)
    
    text = re.sub(r'\s+', ' ', text)
    
    text = remove_ha_sequences(text)
    
    text = re.sub(r'(.)\1+', r'\1\1', text)
    
    text = remove_single_char_words(text)
    
    text = ' '.join([remove_definite_article(word) if len(word) > 4 else word for word in text.split()])
    
    text = remove_custom_arabic_stopwords(text)
    
    return text
