import streamlit as st
import pandas as pd
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

st.set_page_config(page_title="Amazon Food Review Sentiment Analysis", layout="wide")
st.title("🍕 Food Reviews Sentiment Analysis 🍔")
st.write("Enter a food review below to analyze its sentiment.")
review = st.text_area("Type your review here: ✍️", height=150)

if st.button("🔍 Analyze Sentiment"):
    if review.strip():
        sentiment_score = sia.polarity_scores(review)['compound']

        if sentiment_score >= 0.05:
            sentiment = "Positive 😀"
            st.success(f"**Sentiment:** {sentiment} (Score: {sentiment_score:.2f})")
        elif sentiment_score <= -0.05:
            sentiment = "Negative 😡"
            st.error(f"**Sentiment:** {sentiment} (Score: {sentiment_score:.2f})")
        else:
            sentiment = "Neutral 😐"
            st.warning(f"**Sentiment:** {sentiment} (Score: {sentiment_score:.2f})")
    else:
        st.warning("⚠️ Please enter a review before analyzing.")

st.markdown("---")
st.subheader("📂 Upload CSV for Batch Analysis 🗂️")

uploaded_file = st.file_uploader("Upload a CSV file with a column named 'Review'", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if 'Review' not in df.columns:
        st.error("❌ Error: CSV must contain a column named 'Review'. ❌ ")
    else:
        df['Sentiment Score'] = df['Review'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
        df['Sentiment'] = df['Sentiment Score'].apply(lambda x: "Positive 😀" if x >= 0.05 else ("Negative 😡" if x <= -0.05 else "Neutral 😐"))

        st.write("✅ Sentiment Analysis Completed! Here are the results:")
        st.dataframe(df[['Review', 'Sentiment Score', 'Sentiment']])

        st.subheader("📊 Sentiment Distribution 📈")
        sentiment_counts = df['Sentiment'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['#4CAF50', '#FFC107', '#F44336'])
        st.pyplot(fig)

        st.subheader("☁️ Word Cloud of Reviews")
        all_reviews = " ".join(df['Review'].dropna())
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_reviews)

        fig_wc, ax_wc = plt.subplots(figsize=(8, 4))
        ax_wc.imshow(wordcloud, interpolation='bilinear')
        ax_wc.axis('off')
        st.pyplot(fig_wc)


st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        background-color: #f1f1f1;
        font-size: 14px;
        color: #333;
    }
    </style>
    <div class="footer">
        Built with using Streamlit & NLTK
        2025 - Jithnuka - All Right Reservedᣞ
    </div>
    """,
    unsafe_allow_html=True
)
