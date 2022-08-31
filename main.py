import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer

text = open('read.text', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
tokenized_words = word_tokenize(cleaned_text, "english")

final_words = []

for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

        lemma_words = []
        for word in final_words:
            word = WordNetLemmatizer().lemmatize(word)
            lemma_words.append(word)

emotion_list = []
with open('emotions.text', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

            print(emotion_list)
    w = Counter(emotion_list)
    print(w)


    def sentiment_analyse(sentiment_text):
        score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
        if score['neg'] > score['pos']:
            print("Negative Sentiment")
        elif score['neg'] < score['pos']:
            print("Positive Sentiment")
        else:
            print("Neutral Sentiment")


    sentiment_analyse(cleaned_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('SentimentGraph.png')
plt.show()
