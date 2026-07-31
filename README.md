# 📧 Email / SMS Spam Classifier

An interactive Machine Learning web application built with **Streamlit**, **Scikit-Learn**, and **NLTK** that classifies incoming SMS or Email messages as **Spam** or **Not Spam (Ham)**.

---

## 🚀 Live Demo

🔗 **[Click here to open the Live App on Streamlit Cloud](https://sms-spam-classification-javujqevsx6xpirru89f8j.streamlit.app/)**

---

## ✨ Features

- **Instant Spam Detection**: Input any text/email message and get real-time classification.
- **Advanced Text Preprocessing**:
  - Lowercasing & Tokenization using NLTK (`punkt`, `punkt_tab`)
  - Removal of special characters, punctuation, and English stopwords
  - Word Stemming using PorterStemmer
- **Machine Learning Powered**: Uses TF-IDF Vectorization and a trained classification model.
- **Clean UI**: Simple and responsive interface built with Streamlit.

---

## 🛠️ Tech Stack & Libraries

- **Language**: Python 3.x
- **Web Framework**: Streamlit
- **NLP Library**: NLTK (Natural Language Toolkit)
- **Machine Learning**: Scikit-Learn
- **Model Serialization**: Pickle

---

## 📂 Repository Structure

```text
sms-spam-classification/
│── app.py             # Main Streamlit web application logic
│── model.pkl          # Pre-trained machine learning model
│── vectorizer.pkl     # Pre-fitted TF-IDF Vectorizer
│── requirements.txt   # Required Python libraries for Streamlit Cloud
│── .gitignore         # File exclusions for Git tracking
└── README.md          # Project documentation
