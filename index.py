import nltk

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample text to process
text = "I love to learn natural language processing with Python"

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Tag the words with their part of speech
tagged_words = nltk.pos_tag(words)

# Print the tagged words
print(tagged_words)
