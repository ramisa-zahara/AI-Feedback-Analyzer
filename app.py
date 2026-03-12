# app.py
import streamlit as st
from google import genai
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title="AI Customer Feedback Analyzer", layout="wide")

st.markdown(
    """
    <style>
    body {background-color: #f0f2f6;}
    h2 {font-family: 'Arial', sans-serif;}
    .stButton>button {background-color:#4A90E2; color:white; font-weight:bold; height:50px; width:100%;}
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown(
    """
    <div style="background-color:#4A90E2;padding:15px;border-radius:10px;margin-bottom:20px;">
        <h2 style="color:white;text-align:center;">AI Customer Feedback Analyzer</h2>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([3,1])

with col1:
    reviews = st.text_area("Paste customer reviews below:", height=200)

with col2:
    
    st.markdown("<div style='height:80px'></div>", unsafe_allow_html=True)
    analyze = st.button("Analyze Feedback")


if analyze:
    if not reviews.strip():
        st.warning("Please enter at least one review!")
    else:
       
        review_list = [r.strip() for r in reviews.split("\n") if r.strip()]


        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

        
        prompt = f"""
Analyze the following customer reviews and provide:
1. Overall sentiment
2. Main complaints
3. Suggestions for improvement

Reviews:
{reviews}
"""
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        with st.expander("See AI Analysis"):
            st.write(response.text)

       
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

       
        data = {
            "Sentiment": ["Positive", "Negative", "Neutral"],
            "Count": [pos_count, neg_count, neu_count]
        }
        df = pd.DataFrame(data)

    
        fig, ax = plt.subplots(figsize=(4,3))  
        ax.bar(df["Sentiment"], df["Count"], color=["#4A90E2", "#FF6B6B", "#B0B0B0"])  # blue, red, gray
        ax.set_ylabel("Number of Reviews")
        ax.set_title("Sentiment Analysis Chart")
        st.pyplot(fig)

        
        st.info("Tip: Paste one review per line for best results!")
        st.success("AI analysis is complete!")
        st.warning("If many reviews are entered, analysis may take a few seconds.")