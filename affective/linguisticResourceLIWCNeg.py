# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 21:58:36 2017

@author: dadangewp
"""

import codecs
import re
from nltk.stem.porter import PorterStemmer

class LIWCNeg(object):

    liwcneg=[]

    def __init__(self):
        self.liwcneg = []
        stemmer = PorterStemmer()
        #http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010
        file=codecs.open('D:/PhD/RumourEval/Small Project on Stance Detection in Rumour/affectiveResources/LIWC-NEG.txt', encoding='UTF-8')
        for line in file:
            word = line.strip("\r\n")
            word = stemmer.stem(word)
            self.liwcneg.append(word)
        #print(self.liwcpos)    
        self.pattern_split = re.compile(r"\W+")
        return

    def get_liwcneg_sentiment(self,text):
        
        stemmer = PorterStemmer()
        counter=0
        words = self.pattern_split.split(text.lower())
        words = text.split(" ")
        #print (words)
        #print (self.liwcpos)
        for word in words:
            stemmed = stemmer.stem(word)
            #print(stemmed)
            if stemmed in self.liwcneg:
                counter = counter + 1


        return counter


if __name__ == '__main__':
    liwcnegative = LIWCNeg()
    sentiment=liwcnegative.get_liwcneg_sentiment("protest hating")
    print(sentiment)