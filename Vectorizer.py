
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer



#Bag of Words 
def text_vectorizer(text_column): 
    text_values = text_column.values
    tf = CountVectorizer(stop_words='english')
    document_tf_matrix = tf.fit_transform(text_values)
    return tf, document_tf_matrix
#TFIDF
    
def text_tfidf(text_column):
    text_values = text_column.values
    tfidf = TfidfVectorizer(stop_words='english')
    document_tfidf_matrix = tfidf.fit_transform(text_values)
    return tf, document_tfidf_matrix