"""
This is some code to transform a text data into an n-gram bag of words.
"""

from nltk.tokenize import word_tokenize
# nltk.download('punkt')

def tokenizer(df):
    """
    df: pandas dataframe. Data type must be string format.
    return: 2d array with each list corresponding to a tokenized
    """
    tokenized_list = []
    for text in df:
        tokenized_list.append(word_tokenize(text))
    
    return tokenized_list

def n_clustering(tokenized_text,n):
    """
    tokenized_text: list of str.
    n: int, number of words to sequentially cluster
    return: n-clustered text (an n-gram)
    """
    #initialise an empty list that will be returned
    n_clustered_text = []
    
    #For M words, splitting into an n-gram leads to M-(n-1) chunks of words
    n_chunks = len(tokenized_text) - (n-1)
    
    #loop over words in tokenized_text, and append the joined text.
    for i in range(n_chunks):
        chunk = tokenized_text[i:i+n]
        
        #loop over each chunk to create a string
        text_chunk = ''
        #initialise a counter to add space between words
        count = 1
        for word in chunk:
            text_chunk += word 
            if count < n:
                text_chunk += ' '
            count += 1
            
        n_clustered_text.append(text_chunk)
    
    return n_clustered_text
        


def n_gram(df,n):
    """ 
    df: pandas dataframe, each entry of a column corresponds to an individual document. The whole column is the corpus of text.
    n: int, number of words to be included in each block of text.
    """
    #first create bag-of-words, each list contains tokenized text
    tokenized_corpus = tokenizer(df)
    
    #loop over each list and create an new list containing the n-gram
    n_gram_corpus = []
    
    for sub_list in tokenized_corpus:
        n_clustered_text = n_clustering(sub_list,n)
        n_gram_corpus.append(n_clustered_text)
    
    return n_gram_corpus
        
    
    