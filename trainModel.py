from gensim import corpora, models, similarities

dictionary = corpora.Dictionary.load('./mydictionary.dict')
corpus = corpora.MmCorpus('./corpus.mm')

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=200)
corpus_lsi = lsi[corpus_tfidf]

lsi.save('./model.lsi')
