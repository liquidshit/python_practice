import re
import os
# 'bible_word_counter_text.txt' in script-directory is expected
raw_slash = ('\\')
path = os.getcwd() + raw_slash
def_path = (f'{path}bible_word_counter_text.txt')
print(def_path)
# import text file and define .read and .lower
text_file = open(def_path, encoding='utf-8').read().lower()

# ask user to input a word
input_1 = input('Word to search: ').lower()

#find all the occurrences of {word} in text_file
all_words = re.findall(input_1, text_file)

# store and print the length of all_words
number_words = len(all_words)

print(f'in this text file the word "{input_1}" is mentioned {number_words} times')
