from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
from num2words import num2words

from boolean_model import Boolean_Model

import nltk
import os
import string
import numpy as np
import copy
import pandas as pd
import pickle
import re
import math

# adaptado de https://github.com/williamscott701/Information-Retrieval/blob/master/2.%20TF-IDF%20Ranking%20-%20Cosine%20Similarity%2C%20Matching%20Score/TF-IDF.ipynb
class Vectorial_Model:

    def __init__(self, folders,alpha=None):
        # os.system('python -m nltk.downloader stopwords')
        # os.system('python -m nltk.downloader punkt')
        if(type(folders) is str):
            self.folders = os.listdir(folders)
        else:
            self.folders = folders
        if(alpha):
            self.alpha = alpha
        else:
            self.alpha = 0.3
        self.dataset = []
        self.N = len(self.dataset)
        self.processed_title = []
        self.DF = {}
        self.total_vocab_size = len(self.DF)
        self.total_vocab = [x for x in self.DF]
        self.tf_idf = {}
        self.setDataSet()
        self.process_folders_title()
        self.calcule_DF_all_words()
        self.calcule_tf_idf()
    def setDataSet(self):
        for i in self.folders:
            self.dataset.append(i)
        self.N = len (self.dataset)

    def print_doc(self, id):
        print(self.dataset[id])

    def get_doc(self, id):
        return self.dataset[id]

    def convert_lower_case(self, data):
        return np.char.lower(data)

    def remove_stop_words(self, data):
        stop_words = stopwords.words('english')
        words = word_tokenize(str(data))
        new_text = ""
        for w in words:
            if w not in stop_words and len(w) > 1:
                new_text = new_text + " " + w
        return new_text


    def remove_punctuation(self, data):
        symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
        for i in range(len(symbols)):
            data = np.char.replace(data, symbols[i], ' ')
            data = np.char.replace(data, "  ", " ")
        data = np.char.replace(data, ',', '')
        return data

    def remove_apostrophe(self, data):
        return np.char.replace(data, "'", "")

    def stemming(self, data):
        stemmer= PorterStemmer()
        
        tokens = word_tokenize(str(data))
        new_text = ""
        for w in tokens:
            new_text = new_text + " " + stemmer.stem(w)
        return new_text

    def preprocess(self, data):
        data = self.convert_lower_case(data)
        data = self.remove_punctuation(data) #remove comma seperately
        data = self.remove_apostrophe(data)
        # data = self.remove_stop_words(data)
        # data = self.stemming(data)
        # data = self.remove_punctuation(data)
        # data = self.stemming(data) #needed again as we need to stem the words
        # data = self.remove_punctuation(data) #needed again as num2word is giving few hypens and commas fourty-one
        # data = self.remove_stop_words(data) #needed again as num2word is giving stop words 101 - one hundred and one
        return data

    def process_folders_title(self):
        for i in self.dataset[:self.N]:
            text = i
            token = word_tokenize(str(self.preprocess(i)))
            if(token):
                self.processed_title.append(token)
        if(self.N != len(self.processed_title)):
            self.N = len(self.processed_title)
        
    def calcule_DF_all_words(self):
        for i in range(self.N):
            tokens = self.processed_title[i]
            for w in tokens:
                try:
                    if(self.DF.get(w)):
                        self.DF[w].add(i)
                    else:
                        self.DF[w] = {i}
                except:
                    self.DF[w] = {i}
        for i in self.DF:
            self.DF[i] = len(self.DF[i])
        self.total_vocab_size = len(self.DF)
        self.total_vocab = [x for x in self.DF]


    def doc_freq(self,word):
        c = 0
        try:
            c = self.DF[word]
        except:
            pass
        return c


    def calcule_tf_idf(self):
        doc = 0
        for i in range(self.N):
            
            tokens = self.processed_title[i]
            
            counter = Counter(tokens + self.processed_title[i])
            words_count = len(tokens + self.processed_title[i])
            
            for token in np.unique(tokens):
                
                tf = counter[token]/words_count
                df = self.doc_freq(token)
                idf = np.log((self.N+1)/(df+1))
                
                self.tf_idf[doc, token] = tf*idf

            doc += 1

        # Merging the TF-IDF according to weights
        for i in self.tf_idf:
            self.tf_idf[i] *= self.alpha

    def matching_score(self,k, query):
        preprocessed_query = self.preprocess(query)
        tokens = word_tokenize(str(preprocessed_query))

        print("Matching Score")
        print("\nQuery:", query)
        print("")
        print(tokens)
        
        query_weights = {}

        for key in self.tf_idf:
            
            if key[1] in tokens:
                try:
                    query_weights[key[0]] += self.tf_idf[key]
                except:
                    query_weights[key[0]] = self.tf_idf[key]
        
        query_weights = sorted(query_weights.items(), key=lambda x: x[1], reverse=True)

        print("")
        
        l = []
        
        for i in query_weights[:10]:
            l.append(i[0])
        
        print(l)
        

    

    def cosine_sim(self,a, b):
        cos_sim = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
        return cos_sim

    def vectorising_tf_idf(self):
        D = np.zeros((self.N, self.total_vocab_size))
        for i in self.tf_idf:
            try:
                ind = self.total_vocab.index(i[1])
                D[i[0]][ind] = self.tf_idf[i]
            except:
                pass
        return D

    def gen_vector(self, tokens):

        Q = np.zeros((len(self.total_vocab)))
        
        counter = Counter(tokens)
        words_count = len(tokens)

        self.query_weights = {}
        
        for token in np.unique(tokens):
            
            tf = counter[token]/words_count
            df = self.doc_freq(token)
            idf = math.log((self.N+1)/(df+1))

            try:
                ind = self.total_vocab.index(token)
                Q[ind] = tf*idf
            except:
                pass
        return Q

    def cosine_similarity(self, k, query):
        # print("Cosine Similarity")
        preprocessed_query = self.preprocess(query)
        tokens = word_tokenize(str(preprocessed_query))
        
        # print("\nQuery:", query)
        # print("")
        # print(tokens)
        
        d_cosines = []
        
        query_vector = self.gen_vector(tokens)
        D = self.vectorising_tf_idf()
        for d in D:
            d_cosines.append(self.cosine_sim(query_vector, d))
            
        out = np.array(d_cosines).argsort()[-k:][::-1]
        
        return out




if __name__ == "__main__":
    ri = Vectorial_Model('D:\\Imagens\\Mangás')
    # ri = Vectorial_Model('D:\\Imagens\\Mangás')
    Q = ri.cosine_similarity(10, "My Kingdom (Silent War)")
    print("Melhor resultado => " , end='')
    ri.print_doc(Q[0])
    # resultV = ri.get_doc(Q[0])
    # os.system('pause')
    # for i in Q:
    #     ri.print_doc(i)
    bo = Boolean_Model("My Kingdom (Silent War)", 'D:\\Imagens\\Mangás')
    result = bo.corpusAndQuery()
    print(result)

