# encoding=utf-8
# @Author: WenDesi
# @Date:   09-08-16
# @Email:  wendesi@foxmail.com
# @Last modified by:   WenDesi
# @Last modified time: 08-11-16


from gensim.models import word2vec

sentences = word2vec.Text8Corpus(u'corpus.txt')
model = word2vec.Word2Vec(sentences, min_count=1, size=50, window=5, workers=4)
model.similarity()
