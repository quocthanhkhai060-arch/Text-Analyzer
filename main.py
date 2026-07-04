from analyzer import count_characters, count_words, count_sentences

text = input("Enter some text: ")

print(f"Characters: {count_characters(text)}")
print(f"Words: {count_words(text)}")
print(f"Sentences: {count_sentences(text)}")
