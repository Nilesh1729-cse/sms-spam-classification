import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download required NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Please ensure 'vectorizer.pkl' and 'model.pkl' are in the directory.")
    st.stop()

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter your email/sms")

if st.button('Predict'):
    if input_sms.strip():
        # 1. Preprocess
        transformed_text = transform_text(input_sms)

        # 2. Vectorize
        vectorized_text = tfidf.transform([transformed_text])

        # 3. Predict
        result = model.predict(vectorized_text)[0]

        # 4. Display
        if result == 1:
            st.header("Spam Detected")
        else:
            st.header("Not Spam")
    else:
        st.warning("Please enter some text to classify.")
