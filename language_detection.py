# import string, langid, langdetect

from nltk import *
from nltk.corpus import *


def lang_ratio(input):
    lang_ratio = {}
    tokens = wordpunct_tokenize(input)  # tokenize the input to separate word and punctuaction
    words = [word.lower() for word in tokens]  # convert all charaters in token into lowercase
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
        lang_ratio[language] = len(common_elements)
    return lang_ratio


def detect_language(input):
    ratios = lang_ratio(input)
    language = max(ratios, key=ratios.get)  # detect the language based on the ratio
    return language
