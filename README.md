# Startup Pitch Predictor

A machine learning-powered web app that predicts whether a startup pitch will receive funding — based on the pitch text, requested amount, and startup category. Built with scikit-learn and Streamlit, it's a fast, interactive tool for entrepreneurs, investors, or curious minds.

##  What It Does

-  Takes in a startup's elevator pitch
-  Asks how much funding you're requesting
-  Takes your startup category (tech, health, edu, etc.)
- Predicts whether you'd get funding or not
-  Shows prediction instantly in a user-friendly interface

 ## 🛠️ Built With

- Python
- scikit-learn
- Streamlit
- pandas / numpy / joblib
- TF-IDF Vectorizer for NLP

##  How to Run Locally

1. **Clone the repository**
git clone https://github.com/aarushitandon0/startup-pitch-predictor.git
cd startup-pitch-predictor

2. **Install dependencies**
pip install -r requirements.txt

3. **Run the app**
streamlit run app.py

## UI Preview

[![UI Screenshot](https://github.com/aarushitandon0/startup-pitch-predictor/blob/main/Screenshot%202025-05-26%20175140.png?raw=true)](https://github.com/aarushitandon0/startup-pitch-predictor/blob/main/Screenshot%202025-05-26%20175140.png)

## Model Details
Logistic Regression classifier
Trained on startup pitch dataset
Feature engineered with:
1. TF-IDF vectorized pitch text
2. Scaled funding amount
3. Encoded startup category

## Future Improvements
Add live feedback on pitch text

More training data for better accuracy

Advanced NLP models like BERT

Show confidence scores + explainability

