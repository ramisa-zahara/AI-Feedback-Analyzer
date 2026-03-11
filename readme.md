
# AI Customer Feedback Analyzer

A professional **Streamlit application** that analyzes customer reviews using the **Google Gemini API**.  
It provides **overall sentiment analysis**, identifies **main complaints**, suggests **improvements**, and generates a **visual sentiment chart**.

---

## Features

- Analyze multiple customer reviews at once.
- Classify each review as **Positive**, **Negative**, or **Neutral**.
- Generate a **bar chart** visualizing sentiment counts.
- Provide actionable recommendations for product improvement based on customer feedback.
- Responsive and user-friendly UI with a **soothing blue theme**.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/ai-feedback-analyzer.git
cd ai-feedback-analyzer
````

2. Install dependencies:

```bash
python3 -m pip install --upgrade -r requirements.txt
```

*Or install directly:*

```bash
python3 -m pip install --upgrade google-genai streamlit pandas matplotlib
```

---

## Usage

1. Set your **Gemini API key** as an environment variable:

```bash
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

2. Run the Streamlit application:

```bash
streamlit run app.py
```

3. Open the URL displayed in the terminal.
4. Paste customer reviews (one per line) and click **Analyze Feedback**.
5. The application generates:

   * Overall AI analysis
   * Sentiment classification
   * Sentiment chart
   * Suggestions and tips

---

## Requirements

* Python 3.10+
* Streamlit
* pandas
* matplotlib
* google-genai

---

## Deployment

This application can be deployed on **Streamlit** or any cloud platform that supports Python.

### Deploy on Vercel

1. Create a `vercel.json` file in your project root:

```json
{
  "version": 2,
  "builds": [
    { "src": "app.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "app.py" }
  ]
}
```

2. Push your repository to GitHub.
3. Connect the repository to **Vercel**.
4. Deploy following Vercel instructions.
5. Set the **GEMINI_API_KEY** in Vercel environment variables.

---

## How It Works

1. Users paste customer reviews into the input area (one per line).

2. Click **Analyze Feedback**.

3. The app calls the **Google Gemini API** to:

   * Generate overall AI analysis
   * Classify sentiment for each review
   * Display a sentiment chart

4. Actionable suggestions and tips are displayed to improve products and services.
