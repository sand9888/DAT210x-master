import nltk
import pandas as pd
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.stem import PorterStemmer


# reading reviews file and adding column
review_in = pd.read_csv('170413_195458_HotelReviews.csv', sep=';', header=0)
review_in['review_ID'] = review_in.index

# reading SentiWordNet file
from sentiwordnet import SentiWordNetCorpusReader, SentiSynset
swn_filename = 'SentiWordNet_3.0.0_20130122.txt'
posneg_table = SentiWordNetCorpusReader(swn_filename)

# posneg_table = [line.rstrip('\n') for line in open('SentiWordNet_3.0.0_20130122.txt')]
# posneg_table = np.genfromtxt("SentiWordNet_3.0.0_20130122.txt",delimiter=" ")
# posneg_table = open('SentiWordNet_3.0.0_20130122.txt').read().split('\n')
# posneg_table = pd.read_csv('SentiWordNet_3.0.0_20130122.txt', sep='\t', skiprows=32)

# reading stop-words file
stop_words = open('stopwordslist2.txt').read()

# preprocessing columns befor removing stop-words
review_in['Room_Tip'].fillna('', inplace=True)
review_in['Review_Text'] = review_in['Review_Text'].str.lower().str.split()
review_in['Room_Tip'] = review_in['Room_Tip'].str.lower().str.split()
review_in['Review_title'] = review_in['Review_title'].str.lower().str.split()

# removing stop-words
review_in['Review_Text'] = review_in['Review_Text'].apply(lambda x: [item for item in x if item not in stop_words])
review_in['Room_Tip'] = review_in['Room_Tip'].apply(lambda x: [item for item in x if item not in stop_words])
review_in['Review_title'] = review_in['Review_title'].apply(lambda x: [item for item in x if item not in stop_words])

# stemming words
ps = PorterStemmer()
review_in['Review_Text'] = review_in["Review_Text"].apply(lambda x: [ps.stem(y) for y in x])
review_in['Room_Tip'] = review_in['Room_Tip'].apply(lambda x: [ps.stem(y) for y in x])
review_in['Review_title'] = review_in['Review_title'].apply(lambda x: [ps.stem(y) for y in x])

print(posneg_table)