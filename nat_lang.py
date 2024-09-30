import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Ensure necessary NLTK datasets are downloaded
nltk.download('punkt')

def srm_count_words_sentences_paragraphs(text):
    # Tokenize text into words
    words = word_tokenize(text)
    word_count = len(words)

    # Tokenize text into sentences
    sentences = sent_tokenize(text)
    sentence_count = len(sentences)

    # Count paragraphs (consider paragraphs as text separated by two newlines)
    paragraphs = text.split('\n\n')
    paragraph_count = len([p for p in paragraphs if p.strip() != ''])  # Exclude empty paragraphs

    return word_count, sentence_count, paragraph_count

# Example usage
text = """This is a sample text. It contains multiple sentences.

Here is a new paragraph. And another sentence here."""

word_count, sentence_count, paragraph_count = srm_count_words_sentences_paragraphs(text)

print(f"Word Count: {word_count}")
print(f"Sentence Count: {sentence_count}")
print(f"Paragraph Count: {paragraph_count}")
