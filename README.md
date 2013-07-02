gensim_boilerplate
==================

Evangelos Tripolitakis
vtripolitakis@gmail.com

Gensim Python scripts to get started

REQUIREMENTS: Gensim, NumPy, SciPy

```bash
1) add your corpus, one document per line and name it 'inputCorpus.txt'
2) run: python ./createDictionary.py and you'll get a 'mydictionary.dict' dictionary in binary form
3) run: python ./createCorpus.py to get a corpus file named 'corpus.mm'
4) run: python ./trainModel.py to get a Latent Semantic Indexing model named 'model.lsi'
```


Now you're ready to start querying Gensim against your model.

See: http://radimrehurek.com/gensim/tut3.html
