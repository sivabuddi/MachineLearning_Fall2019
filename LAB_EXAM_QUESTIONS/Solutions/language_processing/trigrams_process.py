from nltk import wordpunct_tokenize
from nltk import trigrams, FreqDist
from collections import OrderedDict


def top_ten(input_file):
    input_file_data = open(input_file, 'r')
    whole_string = ""
    write_trigrams_output = open("trigram_repetition_output.txt", "w")

    for sentence in input_file_data:
        whole_string += str(sentence)
    input_file_data.close()

    tokens = wordpunct_tokenize(whole_string)
    fdist = FreqDist(trigrams(tokens))
    sorted_by_value = OrderedDict(sorted(fdist.items(), key=lambda x: x[1], reverse=True))
    i = 0
    trigrams_list = []
    print("\033[93m" + " printing top ten trigrams extracted")
    for key, value in sorted_by_value.items():
        print(key, value)
        trigrams_list.append(str(key))
        write_trigrams_output.write(str(key) + "\t")
        i += 1
        if i > 10:
            break
    sentence_set = set({})
    input_file_data = open(input_file, 'r')
    for sentence in input_file_data:
        list_trigrams_sentence = list(trigrams(wordpunct_tokenize(sentence)))
        for tri_gram in list_trigrams_sentence:
            if str(tri_gram) in trigrams_list:
                sentence_set.add(sentence)

    print(sentence_set)
    print("\033[92m" + "sentences with top 10 repeated trigrams")
    concat_sentences = ""
    write_trigrams_output.write("\n\n" + "writing individual sentences which has high reps of trigrams" + "\n\n")
    for sentence in sentence_set:
        print(sentence)
        concat_sentences += sentence
        write_trigrams_output.write("\n" + sentence)

    print("\033[94m" + "Printing concatenated String")
    print(concat_sentences)
    write_trigrams_output.write("\n" + "writing Concatenated String" + "\n")
    write_trigrams_output.write("\n" + concat_sentences)
