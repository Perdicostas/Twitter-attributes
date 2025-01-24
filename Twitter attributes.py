import csv
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

#Function that NLP processing is applied to all sentences in the given tweet, and it performs a simple tokenization.
def process_tweet_simple_tokenize(text: str):

    processed_tweet = []
    sentences = sent_tokenize(text)
    for sentence in sentences:
        processed_tweet.append(word_tokenize(sentence))
    return processed_tweet

#Function that loads tweets stored in the provided input CSV file.
def load_tweet(file_name, tweet_length_lower_bound: int = 20):
 
    products = []

    with open(file_name, "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)

        for line in reader:
            text = line[0]
            if len(text) < tweet_length_lower_bound:continue
            processed_tweet = process_tweet_simple_tokenize(text)
            products.append(processed_tweet)

    return products

#Load tweets utilizing the simple processor.
fn_tweets=load_tweet('FILE_NAME.csv')

'''This iteration of the method to extract aspects from available tweets emphasizes term frequency 
while also removing stopwords and short words. Furthermore, it calculates a singular, universal set of aspects across all products.'''
def get_aspects(fn_tweets: list, aspect_num: int):
  
    stopLex = set(stopwords.words('english'))
    freq = defaultdict(int)

    for tweet in fn_tweets:
        for sentence in tweet:
            for term in sentence:
                term = term.lower()
                if (term not in stopLex) and len(term) >= 3:
                    freq[term] += 1

    my_top = sorted(freq.items(), key=lambda x:x[1], reverse=True)[:aspect_num]

    return my_top

#You can change the number depending on the number of aspects you want.
fn_aspects=get_aspects(fn_tweets,10)

print(fn_aspects)