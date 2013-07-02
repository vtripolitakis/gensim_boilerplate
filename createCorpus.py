 # -*- coding: utf-8 -*-
import logging
from gensim import corpora, models, similarities

class MyCorpus(object):
    def __iter__(self):
    	di = corpora.Dictionary.load('./mydictionary.dict')
        for line in open('inputCorpus.txt'):
            # assume there's one document per line, tokens separated by whitespace
            yield di.doc2bow(line.lower().split())



corpus_memory_friendly = MyCorpus()

corpora.MmCorpus.serialize('./corpus.mm', corpus_memory_friendly)
