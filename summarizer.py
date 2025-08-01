import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq

# Download required data (only needed once)
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences=3):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    
    freq_table = {}
    for word in words:
        if word.isalpha() and word not in stop_words:
            freq_table[word] = freq_table.get(word, 0) + 1

    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in freq_table:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + freq_table[word]
    
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    return summary

if __name__ == "__main__":
    sample_text = """
    Natural Language Processing (NLP) is a fascinating field of Artificial Intelligence.
    It focuses on the interaction between computers and humans using natural language.
    With the rise of big data, NLP is more important than ever.
    Text summarization is one of its key applications.
    Extractive summarization picks important sentences from the original text.
    Abstractive summarization, on the other hand, generates new sentences.
    Both approaches have their pros and cons.
    """
    summary = summarize_text(sample_text, num_sentences=2)
    print("Summary:")
    print(summary)
