
frequency_of_word = {}
text = input("Text: ")
words = text.split()

for word in words:
    frequency = frequency_of_word.get(word, 0)
    frequency_of_word[word] = frequency + 1

for word, count in frequency_of_word.items():
    print("{0} : {1}".format(word, count))

