from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import re
import string
import os

stemmer = SnowballStemmer('english')


def remove_punctuation(text: str) -> str:
    return ''.join([words for words in text if words not in string.punctuation])


def lowercase(text: str) -> str:
    return text.lower()


def remove_links(text: str) -> str:
    return re.sub('https?://\S+|www\.\S+', '', text)


def remove_words_containing_numbers(text: str) -> str:
    return re.sub('\w*\d\w*', '', text)


def remove_multiple_whitespaces(text: str) -> str:
    return ' '.join(text.split())


def remove_stopwords_and_stem(text: str) -> list[str]:
    text_tokens = word_tokenize(text)
    return [stemmer.stem(word) for word in text_tokens if word not in stopwords.words()]


def clean_text_and_return_tokens(text: str) -> list[str]:
    os.write(1, (text[:10] + '\n').encode())
    text = remove_links(text)
    text = remove_punctuation(text)
    text = lowercase(text)
    text = remove_words_containing_numbers(text)
    text = remove_multiple_whitespaces(text)
    return remove_stopwords_and_stem(text)


# sample = 'Programmers You  234234   have won a Nokia 7250i. This is what you get when you win our FREE auction. To take part send Nokia to 86021 now. https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python/11332580'
# stop_words = set(stopwords.words('english'))
# word_tokens = word_tokenize(sample)
# print(clean_text(sample))
