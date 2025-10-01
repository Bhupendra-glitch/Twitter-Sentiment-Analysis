import streamlit as st
from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_model = pipeline("sentiment-analysis")

# Streamlit UI
st.title("🐦 Twitter Sentiment Analysis")
st.write("Enter a tweet below and analyze its sentiment.")

# User input
tweet = st.text_area("✍️ Type or paste a tweet:")

if st.button("🔍 Analyze Sentiment"):
    if tweet.strip():
        # Check if input has at least one alphabet character
        if any(c.isalpha() for c in tweet):
            # Predict sentiment
            result = sentiment_model(tweet)[0]
            label = result['label']
            score = round(result['score'] * 100, 2)

            # Display results
            st.subheader("📊 Sentiment Result")
            if label == "POSITIVE":
                st.success(f"😊 Positive ({score}%)")
            elif label == "NEGATIVE":
                st.error(f"😡 Negative ({score}%)")
            else:
                st.warning(f"😐 Neutral ({score}%)")
        else:
            st.warning("⚠️ Incorrect / Not valid input")
    else:
        st.warning("⚠️ Please enter a tweet to analyze.")


