# Disaster Tweets Kaggle Competition

https://www.kaggle.com/c/nlp-getting-started

See notebook with proper formatting: https://nbviewer.jupyter.org/github/erick-hm/DisasterTweetsNLP/blob/master/DisasterTweetsNLP_NaiveBayes.ipynb

The notebooks in this repository are submissions to the Kaggle competition, worked on by me only. The competition tasks teams with differentiating a sample of tweets, 
on whether they correspond to real disasters or not. In addition to text data, we also have access to keywords associated to the tweets and location data, 
both with many missing values. The data has a few erroneous entries, with some tweets with the same text carrying both labels for different entries. Nonetheless, this competition provides a
nice introduction to natural language processing.

For my first submission, I have opted for a Naive Bayes text classifier. I then took the prediction probabilities for whether the tweet corresponded to a disaster and did some data engineering
to generate additional features. For example, using sentiment analysis with TextBlob, counting the number of nouns and verbs in each tweet, and looking at the fraction of disasters
associated to each keyword, I was able to feed this additional data into a random forest model which achieved an accuracy of approximately 90% on the validation set. The submission to kaggle
had an f1 score of 0.797 on the unseen test data.

In future updates, I will look to use more advanced language models and go further with the data engineering.


### Prerequisites
Less common libraries that may need to be installed:

Cufflinks

Shap

TextBlob


## Authors

* **Erick Hinds Mingo** 

 
## Acknowledgments
Thanks to the authors of the data for providing a fun competition
