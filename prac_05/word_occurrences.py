
frequency_of_word = {}
text = input("Text: ")
words = text.split()

for word in words:
    frequency = frequency_of_word.get(word, 0)
    frequency_of_word[word] = frequency + 1

