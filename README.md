# 🤖 FAQ Chatbot

A simple and interactive FAQ Chatbot built with Python, Streamlit, and Scikit-learn. It helps users get instant answers to frequently asked questions through a clean and user-friendly chat interface.

## ✨ Features

- 💬 Interactive chatbot interface
- ⚡ Quick questions through the sidebar
- 🧠 NLP-based FAQ matching using TF-IDF
- 🎯 Cosine similarity to find relevant answers
- 💬 Chat history during the session
- 🗑️ Clear conversation option
- 🎨 Custom styling and responsive layout
- 🐍 Built with Python

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Streamlit** — Web application interface
- **Scikit-learn** — Text processing and similarity matching
- **TF-IDF Vectorization** — Converts questions into numerical representations
- **Cosine Similarity** — Matches user questions with stored FAQs

## 📂 Project Structure

```text
CodeAlpha_FAQChatbot/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Uplakshya2005/CodeAlpha_FAQChatbot.git
```

### 2. Open the project folder

```bash
cd CodeAlpha_FAQChatbot
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser. If it does not open automatically, follow the local URL displayed in your terminal.

## 🧠 How It Works

1. The chatbot stores a collection of frequently asked questions and their answers.
2. TF-IDF converts the stored questions into numerical vectors.
3. When a user enters a question, the chatbot converts it into a vector.
4. Cosine similarity compares the new question with the stored questions.
5. The chatbot returns the answer associated with the closest matching question.
6. If the similarity score is too low, the chatbot displays a fallback response.

**Note:** This is a rule-based FAQ chatbot using text similarity. It does not generate answers using a large language model.

## ❓ Example Questions

- What is your name?
- What are your working hours?
- How can I contact support?
- What services do you provide?
- How can I reset my password?
- How do I create an account?
- How does this chatbot work?

## 🔧 Customization

You can customize the chatbot by editing the `faqs` list in `app.py`. Add your own questions and answers to make it suitable for a college project, business, or customer support demo.

## 🚀 Future Improvements

- Add more FAQs and categories
- Support multiple languages
- Store chat history persistently
- Add a database for managing FAQs
- Improve matching for spelling mistakes and differently phrased questions
- Integrate an AI-powered answer system

## 🎓 Project Purpose

This project demonstrates basic Natural Language Processing (NLP), text vectorization, similarity matching, and interactive web application development using Python.

## 👨‍💻 Author

**Uplakshya2005**

GitHub: [@Uplakshya2005](https://github.com/Uplakshya2005)

---

⭐ If you find this project useful, consider giving the repository a star.
