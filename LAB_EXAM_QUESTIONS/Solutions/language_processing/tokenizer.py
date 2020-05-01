from nltk import wordpunct_tokenize, ngrams
from nltk.stem import WordNetLemmatizer


def tokenize(input_file, lemmitization_file, trigrams_file, token_file):
    lemmetizer = WordNetLemmatizer()
    in_file_data = open(input_file, 'r')
    lem_file_out = open(lemmitization_file, 'a+')
    trigrams_file_out = open(trigrams_file, 'a+')
    token_file_out = open(token_file, 'a+')
    for sentence in in_file_data:
        tokens = wordpunct_tokenize(str(sentence))
        token_file_out.write(str(tokens) + "\n")
        trigrams = ngrams(tokens, 3)
        trigrams_file_out.write(str(list(trigrams)) + "\n")
        for token in tokens:
            lem_file_out.write(lemmetizer.lemmatize(token) + "\t")
        lem_file_out.write("\n")
    in_file_data.close()
    lem_file_out.close()
    trigrams_file_out.close()
    token_file_out.close()
