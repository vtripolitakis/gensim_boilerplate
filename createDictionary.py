 # -*- coding: utf-8 -*-
import logging
from gensim import corpora, models, similarities

stoplist = set('for a of the and to in και ο ή η το των τον τους τουσ τις τισ τα να στον στην στο ωσ ως με αυτός αυτόσ αυτοσ αυτος αυτη αυτή αυτο αυτό εκείνος εκείνοσ εκεινος εκεινος εκείνη εκεινη εκεινο εκεινο για μη δε δια ανά ανα κατά κατα υπερ υπέρ'.split())

lineArray = [line.lower().split() for line in open('koko.txt')]
dictionary = corpora.Dictionary(lineArray)
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]

once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids)
dictionary.compactify()

dictionary.save('./mydictionary.dict')
