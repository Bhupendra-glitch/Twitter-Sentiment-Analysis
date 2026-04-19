import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_sentiment_model():
    """Load the sentiment analysis pipeline once and reuse it."""
    return pipeline("sentiment-analysis")

@st.cache_data
def clean_tweet(text: str) -> str:
    """Return cleaned tweet text or an empty string if no valid content exists."""
    normalized = text.strip()
    if not normalized:
        return ""
    return normalized

@st.cache_data
def has_alpha(text: str) -> bool:
    """Detect whether the tweet contains at least one alphabetic character."""
    return any(c.isalpha() for c in text)

def analyze_sentiment(model, text: str) -> dict:
    """Analyze sentiment and return label + confidence score."""
    result = model(text)[0]
    return {
        "label": result["label"],
        "score": round(result["score"] * 100, 2),
    }

def render_result(label: str, score: float) -> None:
    """Render the sentiment prediction with an icon and styling."""
    st.subheader("📊 Sentiment Result")
    if label == "POSITIVE":
        st.success(f"😊 Positive — {score}% confidence")
    elif label == "NEGATIVE":
        st.error(f"😡 Negative — {score}% confidence")
    else:
        st.info(f"😐 Neutral — {score}% confidence")

def main() -> None:
    st.set_page_config(
        page_title="Twitter Sentiment Analysis",
        page_icon="🐦",
        layout="centered",
    )

    st.title("🐦 Twitter Sentiment Analysis")
    st.write(
        "Paste a tweet below and use a transformer-based model to estimate whether the sentiment is positive, negative, or neutral."
    )

    st.sidebar.header("How it works")
    st.sidebar.write(
        "This app uses the Hugging Face `transformers` sentiment-analysis pipeline. "
        "It loads the model once and reuses it for faster predictions."
    )
    st.sidebar.write(
        "Enter a tweet, then click the button to see the sentiment label and confidence score."
    )

    tweet = st.text_area(
        "✍️ Type or paste a tweet:",
        placeholder="e.g. Just tried the new app and it made my day!",
        height=180,
    )

    if st.button("🔍 Analyze Sentiment"):
        cleaned_text = clean_tweet(tweet)
        if not cleaned_text:
            st.warning("⚠️ Please enter a tweet to analyze.")
            return

        if not has_alpha(cleaned_text):
            st.warning("⚠️ Please enter a valid tweet containing text.")
            return

        try:
            sentiment_model = load_sentiment_model()
            prediction = analyze_sentiment(sentiment_model, cleaned_text)
            render_result(prediction["label"], prediction["score"])
        except Exception as exc:
            st.error("❌ Unable to analyze sentiment right now. Please try again later.")
            st.exception(exc)

    with st.expander("💡 Tips for better results"):
        st.markdown(
            "- Keep the tweet text short and focused.\n"
            "- Avoid entering only URLs or emojis.\n"
            "- The model works best with natural language input."
        )

if __name__ == "__main__":
    main()


