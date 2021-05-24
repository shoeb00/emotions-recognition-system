from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import string
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def sentiment_analyze(input_text):

    text = input_text

    lower_text = text.lower()
    cleaned_text = lower_text.translate(
        str.maketrans('', '', string.punctuation))

    tokenized_words = word_tokenize(cleaned_text, "english")

    final_words = ''
    for word in tokenized_words:
        if word not in stopwords.words('english'):
            final_words += word + ' '
    score = SentimentIntensityAnalyzer().polarity_scores(input_text)
    print(score)

    emotions = ['Positive', 'Negative', 'Neutral', 'Compound']
    scores = [score['pos'], score['neg'], score['neu'], abs(score['compound'])]
    positions = [0, 1, 2, 3]

    plt.bar(positions, scores, width=0.5)
    plt.xticks(positions, emotions)
    loc = './media/graph.png'
    if os.path.isfile(loc):
        os.remove(loc)
    plt.savefig(loc)
    plt.show()
    plt.close()
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        # print('neg')
        return "Negative Sentiment"
    elif pos > neg:
        # print('pos')
        return "Positive Sentiment"
    else:
        # print('neu')
        return "Neutral Vibe"


# sentiment_analyze('I am really hungry and sad')
