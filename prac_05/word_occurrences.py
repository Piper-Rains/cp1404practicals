
word_to_frequency = {}
text = input("Text: ")
words = text.split()

for word in words:
    frequency = word_to_frequency.get(word, 0)
    word_to_frequency[word] = frequency + 1

# for word, count in frequency_of_word.items():
#     print("{0} : {1}".format(word, count))

words = list(word_to_frequency.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_frequency[word]))
