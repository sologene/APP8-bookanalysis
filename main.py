
import re, nltk
nltk.download('stopwords')
nltk.download('sentiment')
nltk.download('vader_lexicon')
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer


analyser = SentimentIntensityAnalyzer()
english_stopwords = stopwords.words("english")

with open("miracle_in_the_andes.txt", "r", encoding="UTF-8") as file:
    book = file.read()

# pattern = re.compile("[a-zA-z]+")
# findings = re.findall(pattern, book.lower())

pattern = re.compile("Chapter [0-9]+")
findings = re.findall(pattern, book.lower())
chapters = re.split(pattern, book)
chapters = chapters[1:]

for chapter in chapters:
    score = analyser.polarity_scores(chapter)
    print(score)




d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value, key)  for (key, value) in d.items()]
d_list = sorted(d_list, reverse=True)

filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))
print(english_stopwords)