
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #f5f7ff, #eef3ff, #fafbff);
    color: #172554;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffffff, #eff4ff);
    border-right: 1px solid #dfe8ff;
}

.hero {
    background: linear-gradient(120deg, #13285b, #2563eb, #7561f9);
    padding: 30px;
    border-radius: 24px;
    color: white;
    margin-bottom: 24px;
    box-shadow: 0 14px 35px rgba(37, 99, 235, 0.18);
}

.hero h1 {
    color: white;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero p {
    color: #e5edff;
    font-size: 16px;
    margin: 0;
}

.section-title {
    color: #172554;
    font-size: 20px;
    font-weight: 800;
}

.small-muted {
    color: #64748b;
    font-size: 13px;
}

.info-card {
    background: white;
    border: 1px solid #e0e9ff;
    border-radius: 18px;
    padding: 16px;
    margin-top: 14px;
    box-shadow: 0 5px 18px rgba(37, 99, 235, 0.05);
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: 1px solid #dce6ff;
    background: white;
    color: #1e3a8a;
    font-weight: 600;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: #edf4ff;
    border-color: #7da5ff;
    color: #1d4ed8;
}

[data-testid="stChatMessage"] {
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid #e0e9ff;
    border-radius: 18px;
    padding: 14px;
    box-shadow: 0 5px 16px rgba(30, 64, 175, 0.04);
    margin-bottom: 10px;
}

[data-testid="stChatInput"] {
    border: 1px solid #d7e4ff;
    border-radius: 18px;
    background: white;
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.07);
}

.footer {
    text-align: center;
    color: #8190b3;
    font-size: 13px;
    padding: 20px 0 5px;
}

.online-pill {
    display: inline-block;
    padding: 7px 12px;
    border-radius: 30px;
    background: #dcfce7;
    color: #166534;
    font-weight: 700;
    font-size: 12px;
}
/* Chat input border colour */
[data-testid="stChatInput"] {
    border: 3px solid #00BFFF !important;
    border-radius: 18px !important;
    background-color: #FFFFFF !important;
}

/* Typed question */
[data-testid="stChatInput"] textarea {
    color: #111111 !important;
    -webkit-text-fill-color: #111111 !important;
    caret-color: #00BFFF !important;
}

/* Placeholder */
[data-testid="stChatInput"] textarea::placeholder {
    color: #64748B !important;
    opacity: 1 !important;
}

/* Border when clicked */
[data-testid="stChatInput"]:focus-within {
    border-color: #00BFFF !important;
    box-shadow: 0 0 0 2px rgba(0, 191, 255, 0.2) !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- FAQ DATABASE ----------------
faqs = [
    {
        "question": "What is your name?",
        "answer": "Hi! 🤖 I am FAQ Bot, your friendly virtual assistant. How can I help you today?"
    },
    {
        "question": "What are your working hours?",
        "answer": "Our sample working hours are Monday to Friday, 9 AM to 5 PM."
    },
    {
        "question": "How can I contact support?",
        "answer": "You can contact our support team at support@example.com. Replace this sample email with your real support email."
    },
    {
        "question": "What services do you provide?",
        "answer": "I can answer frequently asked questions about services, accounts, working hours and customer support."
    },
    {
        "question": "How can I reset my password?",
        "answer": "Click on the Forgot Password option on your login page and follow the instructions to reset your password."
    },
    {
        "question": "Is your service free?",
        "answer": "This is a demo FAQ answer. Add your actual pricing and subscription details here."
    },
    {
        "question": "How do I create an account?",
        "answer": "Open the registration page, fill in the required information and follow the instructions to create your account."
    },
    {
        "question": "Where are you located?",
        "answer": "Please add your organization's location and contact information to this FAQ answer."
    },
    {
        "question": "What technologies are used in this chatbot?",
        "answer": "This chatbot uses Python, Streamlit and Scikit-learn. TF-IDF and cosine similarity help it find relevant FAQ answers."
    },
    {
        "question": "How does this chatbot work?",
        "answer": "I compare your question with stored FAQ questions using TF-IDF and cosine similarity, then return the answer for the closest match. I do not generate answers like a general-purpose AI model."
    },
    {
        "question": "Thank you",
        "answer": "You're welcome! 😊 Feel free to ask me another question."
    },
    {
        "question": "Goodbye",
        "answer": "Goodbye! 👋 Thanks for chatting with FAQ Bot. Have a wonderful day!"
    },
]

# ---------------- NLP MODEL ----------------
faq_questions = [faq["question"] for faq in faqs]

vectorizer = TfidfVectorizer(
    lowercase=True,
    strip_accents="unicode",
    ngram_range=(1, 2),
    sublinear_tf=True,
)

faq_vectors = vectorizer.fit_transform(faq_questions)


def get_answer(user_question):
    """Find the closest FAQ question and return its answer."""
    question = user_question.strip()

    if not question:
        return "Please type a question so I can help. 🙂"

    user_vector = vectorizer.transform([question])
    scores = cosine_similarity(user_vector, faq_vectors)[0]

    best_index = int(scores.argmax())
    best_score = float(scores[best_index])

    if best_score < 0.20:
        return (
            "Sorry, I couldn't find a relevant answer. 💡\n\n"
            "Try asking about working hours, support, password reset, "
            "accounts or our services."
        )

    return faqs[best_index]["answer"]


# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi there! 👋 Welcome to FAQ Bot. Ask me anything about our services, accounts or support."
        }
    ]

if "pending_question" not in st.session_state:
    st.session_state.pending_question = None


def select_question(question):
    st.session_state.pending_question = question


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("""
    <div style="padding:8px 0 18px;">
        <div style="font-size:42px;">🤖</div>
        <div style="font-size:25px;font-weight:800;color:#172554;">FAQ Bot</div>
        <div style="color:#64748b;font-size:13px;">Your friendly help assistant</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">⚡ Quick Questions</div>',
        unsafe_allow_html=True,
    )
    st.caption("Click a question to start chatting.")

    suggested_questions = [
        "What is your name?",
        "What are your working hours?",
        "How can I contact support?",
        "What services do you provide?",
        "How can I reset my password?",
        "How do I create an account?",
        "How does this chatbot work?",
    ]

    for i, question in enumerate(suggested_questions):
        st.button(
            question,
            key=f"quick_question_{i}",
            use_container_width=True,
            on_click=select_question,
            args=(question,),
        )

    st.markdown("---")
    st.markdown(
        '<div class="section-title">✨ Features</div>',
        unsafe_allow_html=True,
    )

    st.markdown("""
    <div class="info-card">
        <p>✅ Quick FAQ answers</p>
        <p>✅ Similar question matching</p>
        <p>✅ Interactive chat history</p>
        <p>✅ NLP with TF-IDF</p>
        <p>✅ Simple, responsive interface</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Conversation cleared! 👋 What would you like to know?"
            }
        ]
        st.session_state.pending_question = None
        st.rerun()

    st.markdown(
        '<div class="footer">Made with Python 💙</div>',
        unsafe_allow_html=True,
    )

# ---------------- MAIN HEADER ----------------
st.markdown("""
<div class="hero">
    <div style="font-size:13px;font-weight:700;letter-spacing:1px;
                color:#c8dcff;margin-bottom:10px;">
        ✨ YOUR VIRTUAL SUPPORT ASSISTANT
    </div>
    <h1>FAQ Chatbot 🤖</h1>
    <p>Got a question? Let's find the answer together.</p>
    <p style="margin-top:8px;font-size:14px;">
        Ask naturally, or choose one of the quick questions from the sidebar.
    </p>
</div>
""", unsafe_allow_html=True)

header_left, header_right = st.columns([3, 1])

with header_left:
    st.markdown(
        '<div class="section-title">💬 Chat with your assistant</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="small-muted">FAQ matching mode · Replies instantly</div>',
        unsafe_allow_html=True,
    )

with header_right:
    st.markdown(
        '<div style="text-align:right;"><span class="online-pill">● Online</span></div>',
        unsafe_allow_html=True,
    )

st.write("")

# ---------------- DISPLAY CHAT HISTORY ----------------
for message in st.session_state.messages:
    avatar = "🧑" if message["role"] == "user" else "🤖"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# ---------------- HANDLE USER INPUT ----------------
typed_question = st.chat_input("Type your question here...")

# Sidebar questions take priority over typed input for this rerun.
prompt = st.session_state.pending_question

if prompt is not None:
    st.session_state.pending_question = None
elif typed_question:
    prompt = typed_question

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    answer = get_answer(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(answer)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    FAQ Chatbot Demo · Built with 💙 using Python, Streamlit and Scikit-learn
</div>
""", unsafe_allow_html=True)
