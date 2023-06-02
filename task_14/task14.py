from nltk.tokenize import word_tokenize
from collections import Counter
import os
from math import log2
import pickle


class TFIDFCalculator:
    def __init__(self, path_to_corpus):
        self.__path_to_corpus = path_to_corpus
        if os.path.exists('idf_values.pickle'):
            with open('idf_values.pickle', 'rb') as f:
                self.__idf_values = pickle.load(f)
        else:
            self.__idf_values = self.__inverse_document_frequency

    def __term_frequency(self, text: str) -> dict:
        text = text.lower()
        text = word_tokenize(text)
        text_counter = Counter(text)
        tf_values = {}
        for word in text_counter:
            tf_values[word] = text_counter[word] / len(text)
        return tf_values

    @property
    def __inverse_document_frequency(self):
        list_of_corpus_files = os.listdir(self.__path_to_corpus)
        number_of_documents = len(list_of_corpus_files)
        all_words = []
        for file in list_of_corpus_files:
            with open(os.path.join(self.__path_to_corpus, file), 'r', encoding='windows=1251') as corpus_file:
                text = corpus_file.read()
                text = word_tokenize(text.lower())
                unique_words = set(text)
                all_words.extend(unique_words)
        frequency_values = Counter(all_words)
        idf_values = {}
        for word in frequency_values:
            idf_values[word] = log2(number_of_documents / frequency_values[word])
        with open('idf_values.pickle', 'wb') as idf_pickle:
            pickle.dump(idf_values, idf_pickle)
        return idf_values

    def tf_idf(self, text: str) -> dict:
        idf_values = {}
        tf_values = self.__term_frequency(text)
        for word in tf_values:
            idf_values[word] = tf_values[word] * self.__idf_values.get(word, 0)
        return idf_values