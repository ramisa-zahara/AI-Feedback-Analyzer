import streamlit as st
from google import genai
import pandas as pd
import matplotlib.pyplot as plt

st.title("AI Customer Feedback Analyzer")
st.write("Paste customer reviews below:")

reviews = st.text_area("Customer Reviews", height=200)

if st.button("Analyze Feedback"):
    if not reviews.strip():
        st.warning("Please enter at least one review!")
    else:
        # Split reviews by line
        review_list = [r.strip() for r in reviews.split("\n") if r.strip()]

        # Create Gemini client (reads GEMINI_API_KEY from environment)
        client = genai.Client()

        # Generate overall AI analysis for all reviews
        prompt = f"""
Analyze the following customer reviews and provide:
1. Overall sentiment
2. Main complaints
3. Suggestions for improvement

Reviews:
{reviews}
"""
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        st.subheader("AI Analysis")
        st.write(response.text)

        # --- Generate sentiment counts for chart ---
        pos_count = 0
        neg_count = 0
        neu_count = 0

        for review in review_list:
            sentiment_prompt = f"Classify the sentiment of this review as Positive, Negative, or Neutral:\n\n{review}"
            sentiment_resp = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=sentiment_prompt
            )
            sentiment = sentiment_resp.text.strip().lower()
            if "positive" in sentiment:
                pos_count += 1
            elif "negative" in sentiment:
                neg_count += 1
            else:
                neu_count += 1

        # Create chart
        data = {
            "Sentiment": ["Positive", "Negative", "Neutral"],
            "Count": [pos_count, neg_count, neu_count]
        }
        df = pd.DataFrame(data)

        fig, ax = plt.subplots()
        ax.bar(df["Sentiment"], df["Count"], color=["green", "red", "gray"])
        ax.set_ylabel("Number of Reviews")
        ax.set_title("Sentiment Analysis Chart")
        st.pyplot(fig)