'''
Problem 7 : Language processing
Write a program in which take an Input file, use the simple approach below to summarize a text file:
Link to input file: https://umkc.box.com/s/7by0f4540cdbdp3pm60h5fxxffefsvrw
a. Read the data from a file
b. Tokenize the text into words and apply lemmatization technique on each word.
c. Find all the trigrams for the words.
d. Extract the top 10 of the most repeated trigrams based on their count.
e. Go through the text in the file
f. Find all the sentences with the most repeated tri-grams
g. Extract those sentences and concatenate
h. Print the concatenated result
'''

from language_processing.tokenizer import tokenize
from language_processing.trigrams_process import top_ten
'a,b,c'
tokenize("nlp_input.txt", "lem_output.txt", "trigrams_output.txt", "token_output.txt")

'd,e,f,g,h'
top_ten("nlp_input.txt")