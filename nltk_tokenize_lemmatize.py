from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from part_of_speech import get_part_of_speech
import re

lemmatizer = WordNetLemmatizer()

oprah_wiki = '<p>Working in local media, she was both the youngest news anchor and the first black female news anchor at Nashville\'s WLAC-TV. </p>'

rexed = re.sub(r'/', '', oprah_wiki)
rexed2 = re.sub(r'<p>', '', rexed)
rexed3 = re.sub(r"'", '', rexed2)
tokenized_o = word_tokenize(rexed3)

test = [lemmatizer.lemmatize(token) for token in tokenized_o]

def liner():
  for word in test:
    print(f'{word}')
  return
liner()

print(test)

print(tokenized_o)
