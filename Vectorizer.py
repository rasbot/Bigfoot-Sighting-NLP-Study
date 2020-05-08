#Bag of Words 
from sklearn.feature_extraction.text import CountVectorizer

tf = CountVectorizer()

document_tf_matrix = tf.fit_transform(corpus).todense()

print(sorted(tf.vocabulary_))
print(document_tf_matrix)


#TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
document_tfidf_matrix = tfidf.fit_transform(corpus)
print(sorted(tfidf.vocabulary_))
print(document_tfidf_matrix.todense())