import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import sent_tokenize , word_tokenize
import glob
import re
import os
import numpy as np
import sys
Stopwords = set(stopwords.words('english'))


class Boolean_Model:
    def __init__(self, query, folder):
        self.all_words = []
        self.dict_global = {}
        if type(folder) is str:
            self.file_folder = os.listdir(folder)
        else:
            self.file_folder = folder
        self.idx = 1
        self.files_with_index = {}
        self.query = query
        # os.system('python -m nltk.downloader stopwords')
        # os.system('python -m nltk.downloader punkt')

    def finding_all_unique_words_and_freq(self,words):
        words_unique = []
        word_freq = {}
        for word in words:
            if word not in words_unique:
                words_unique.append(word)
        for word in words_unique:
            word_freq[word] = words.count(word)
        return word_freq
        
    def finding_freq_of_word_in_doc(self,word,words):
        freq = words.count(word)

    def remove_special_characters(self,text):
        regex = re.compile('[^a-zA-Z0-9\s]')
        text_returned = re.sub(regex,'',text)
        return text_returned

    class Node:
        def __init__(self ,docId, freq = None):
            self.freq = freq
            self.doc = docId
            self.nextval = None

    class SlinkedList:
        def __init__(self ,head = None):
            self.head = head
    def corpusAndQuery(self):
        # for file in glob.glob(file_folder):
        for file in self.file_folder:
            # print(file)
            fname = file
            # file = open(file , "r", encoding="utf8")
            # text = file.read()
            text = fname
            text = self.remove_special_characters(text)
            text = re.sub(re.compile('\d'),'',text)
            sentences = sent_tokenize(text)
            words = word_tokenize(text)
            words = [word for word in words]
            words = [word.lower() for word in words]
            words = [word for word in words if word not in Stopwords]
            self.dict_global.update(self.finding_all_unique_words_and_freq(words))
            self.files_with_index[self.idx] = os.path.basename(fname)
            self.idx = self.idx + 1

        unique_words_all = set(self.dict_global.keys())

        linked_list_data = {}
        for word in unique_words_all:
            linked_list_data[word] = self.SlinkedList()
            linked_list_data[word].head = self.Node(1,self.Node)
            word_freq_in_doc = {}
        self.idx = 1
        # for file in glob.glob(file_folder):
        for file in self.file_folder:
            # file = open(file, "r", encoding="utf8")
            # text = file.read()
            fname = file
            text = fname
            text = self.remove_special_characters(text)
            text = re.sub(re.compile('\d'),'',text)
            sentences = sent_tokenize(text)
            words = word_tokenize(text)
            words = [word for word in words]
            words = [word.lower() for word in words]
            words = [word for word in words if word not in Stopwords]
            word_freq_in_doc = self.finding_all_unique_words_and_freq(words)
            for word in word_freq_in_doc.keys():
                try:
                    linked_list = linked_list_data[word].head
                    while linked_list.nextval is not None:
                        linked_list = linked_list.nextval
                    linked_list.nextval = self.Node(self.idx ,word_freq_in_doc[word])
                except:
                    pass
            self.idx = self.idx + 1

        # query = input('Enter your query: ')
        self.query = self.remove_special_characters(self.query)
        self.query = self.query.split(' ')
        self.query = ' and '.join(self.query)
        self.query = word_tokenize(self.query)
        connecting_words = []
        cnt = 1
        different_words = []
        for word in self.query:
            if word.lower() != "and" and word.lower() != "or" and word.lower() != "not":
                different_words.append(word.lower())
            else:
                connecting_words.append(word.lower())
        # print(connecting_words)
        total_files = len(self.files_with_index)
        zeroes_and_ones = []
        zeroes_and_ones_of_all_words = []
        # print(unique_words_all)
        for word in (different_words):
            if word.lower() in unique_words_all:
                zeroes_and_ones = [0] * total_files
                linkedlist = linked_list_data[word].head
                # print(word)
                while linkedlist.nextval is not None:
                    zeroes_and_ones[linkedlist.nextval.doc - 1] = 1
                    linkedlist = linkedlist.nextval
                zeroes_and_ones_of_all_words.append(zeroes_and_ones)
            else:
                continue
                # zeroes_and_ones = [0] * total_files
                # linkedlist = linked_list_data[word].head
                # # print(word)
                # while linkedlist.nextval is not None:
                #     zeroes_and_ones[linkedlist.nextval.doc - 1] = 1
                #     linkedlist = linkedlist.nextval
                # zeroes_and_ones_of_all_words.append(zeroes_and_ones)
        # print(zeroes_and_ones_of_all_words)
        for word in connecting_words:
            try:
                word_list1 = zeroes_and_ones_of_all_words[0]
                word_list2 = zeroes_and_ones_of_all_words[1]
            except:
                continue
            if word == "and":
                bitwise_op = [w1 & w2 for (w1,w2) in zip(word_list1,word_list2)]
                zeroes_and_ones_of_all_words.remove(word_list1)
                zeroes_and_ones_of_all_words.remove(word_list2)
                zeroes_and_ones_of_all_words.insert(0, bitwise_op)
            elif word == "or":
                bitwise_op = [w1 | w2 for (w1,w2) in zip(word_list1,word_list2)]
                zeroes_and_ones_of_all_words.remove(word_list1)
                zeroes_and_ones_of_all_words.remove(word_list2)
                zeroes_and_ones_of_all_words.insert(0, bitwise_op)
            elif word == "not":
                bitwise_op = [not w1 for w1 in word_list2]
                bitwise_op = [int(b == True) for b in bitwise_op]
                zeroes_and_ones_of_all_words.remove(word_list2)
                zeroes_and_ones_of_all_words.remove(word_list1)
                bitwise_op = [w1 & w2 for (w1,w2) in zip(word_list1,bitwise_op)]
                
            zeroes_and_ones_of_all_words.insert(0, bitwise_op)

        files = []    
        # print(zeroes_and_ones_of_all_words)
        if(zeroes_and_ones_of_all_words):
            lis = zeroes_and_ones_of_all_words[0]
            cnt = 1
            for index in lis:
                if index == 1:
                    files.append(self.files_with_index[cnt])
                cnt = cnt+1
                # print(files)

        # print('Melhor resultado: {}'.format(files[0]))
        if(files):
            return files[0]
        else:
            return None

# if __name__ == "__main__":
#     ri = Boolean_Model('Ueno-san wa Bukiyou', 'D:\\Imagens\\Mangás')
#     result = ri.corpusAndQuery()
#     print(result) 