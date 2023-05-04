import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from tkinter import *


def generate_chart():
    text = input_text.get("1.0", END)
    lower_case = text.lower()
    cleaned_text = lower_case.translate(
        str.maketrans('', '', string.punctuation))

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
    with open('emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(
                ",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in lemma_words:
                emotion_list.append(emotion)

    w = Counter(emotion_list)

    fig, ax1 = plt.subplots()
    ax1.bar(w.keys(), w.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    plt.show()


root = Tk()
root.title("Sentiment Analysis")
root.geometry("500x600")

title_label = Label(
    root, text="Sentiment Analysis Chart Generator", font=("Helvetica", 20))
title_label.pack(pady=20)

input_text = Text(root, height=10, width=50, font=("Helvetica", 12))
input_text.pack(pady=10)

generate_button = Button(root, text="Generate Chart", command=generate_chart, font=(
    "Helvetica", 14), bg="#4CAF50", fg="white", padx=10, pady=10)
generate_button.pack(pady=20)

root.mainloop()