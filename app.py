import streamlit as st
import pandas as pd
import joblib
import time

def flatten_array(x):
    return x.values.ravel()

st.markdown(
    """
    <style>
    /* Global styles */
    html, body, .stApp {
        background: linear-gradient(135deg, #FFF5E1, #E3F2FD) !important;
        background-attachment: fixed;
        font-family: 'Segoe UI', sans-serif;
        color: black !important;
        font-size: 18px !important;
    }

    /* General text */
    p, label, span, div, section, small, .stMarkdown, .stText {
        font-size: 18px !important;
        color: black !important;
    }

    /* Headers */
    h1 {
        font-size: 40px !important;
        color: black !important;
    }
    h2 {
        font-size: 32px !important;
        color: black !important;
    }
    h3 {
        font-size: 26px !important;
        color: black !important;
    }

    /* Textarea */
    textarea {
        background-color: #ffffff !important;
        border: 1px solid #ced4da !important;
        border-radius: 0.5rem !important;
        padding: 1rem !important;
        font-size: 18px !important;
        color: black !important;
    }

    /* Selectbox container */
    div.stSelectbox > div[role="combobox"] > div:first-child {
        background-color: black !important;
        color: white !important;
        border: 1px solid #ced4da !important;
        border-radius: 0.5rem !important;
        padding: 0.5rem 1rem !important;
    }

    /* Selectbox text input */
    div.stSelectbox > div[role="combobox"] > input {
        background-color: black !important;
        color: white !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Dropdown menu (listbox) */
    div[role="listbox"] {
        background-color: black !important;
        border-radius: 0.5rem !important;
        border: 1px solid #ced4da !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    /* Dropdown options */
    div[role="option"] {
        background-color: black !important;
        color: white !important;
        padding: 0.5rem 1rem !important;
    }
    div[role="option"]:hover {
        background-color: #e6f0ff !important;
        color: black !important;
        cursor: pointer;
    }

    /* Button */
    div.stButton > button {
        background-color: black !important;
        color: white !important;
        border: 1px solid #ced4da !important;
        border-radius: 0.5rem !important;
        padding: 0.5rem 1.25rem !important;
        font-size: 18px !important;
        cursor: pointer;
        transition: background-color 0.2s ease;
    }
    div.stButton > button:hover {
        background-color: #e6f0ff !important;
        color: black !important;
    }

    /* Force text color inside dropdown/selectbox and button */
    div.stSelectbox * {
        color: white !important;
    }
    div.stButton * {
        color: white !important;
    }

    /* Footer */
    footer {
        color: #999;
        font-size: 16px;
        text-align: center;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Cache model loading so it’s fast after first load
@st.cache_resource(show_spinner=True)
def load_model():
    return joblib.load(r'C:\Users\AARUSHI TANDON\OneDrive\Python\Startup pitch\startup_pitch_model.pkl')

model = load_model()

# Title with emoji and style
st.markdown("<h1 style='text-align:center; color:#4CAF50;'>💡 Startup Pitch Funding Predictor 🚀</h1>", unsafe_allow_html=True)
st.markdown("---")

st.write("### Tell me about your startup and I'll guess if you'll get funded! 🎯")
with st.expander("💡 Tips for Writing a Strong Pitch"):
    st.write("""
    - Be clear about your value proposition.
    - Explain the problem you're solving.
    - Show traction, market size, and uniqueness.
    """)

with st.form(key='pitch_form'):
    pitch_text = st.text_area(
        "📝 **Enter your Startup Pitch Description:**",
        height=180,
        max_chars=1200,
        placeholder="Explain your startup idea clearly, what problem it solves, and why it’s awesome...",
        help="Be honest, detailed but concise!"
    )
    ask_amount = st.slider(
        "💰 **Funding Amount Requested (USD):**",
        min_value=0.0,
        max_value=1000000.0,
        step=500.0,
        format="$%d",
        help="How much money are you asking for?"
    )
    industry = st.selectbox(
        "🏭 **Select Industry:**",
        options=["Tech", "Food", "Healthcare", "Finance", "Education", "Health/Wellness", "Fashion/Beauty", 
                 "Fitness/Sports", "Media/ Entertainment", "Lifestyle/Home", "Travel", "Green/CleanTech", "Electronics", "Others"],
        help="Pick the closest industry for your startup."
    )

    submit_button = st.form_submit_button("🚀 Predict Funding Outcome")

if submit_button:
    # Input validation with cool animated warnings
    if not pitch_text.strip():
        st.warning("⚠️ Oops! Your pitch description can't be empty. Pour your heart out! 💬")
    elif ask_amount <= 0:
        st.warning("⚠️ Funding amount must be greater than zero! 💸")
    elif not industry.strip():
        st.warning("⚠️ Please select an industry. Don't leave me guessing! 🤔")
    else:
        input_df = pd.DataFrame({
            'text': [pitch_text],
            'Original Ask Amount': [ask_amount],
            'Industry': [industry]
        })

        # Fun loading bar animation
        progress_text = "Crunching numbers, analyzing your pitch... ⏳"
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(101):
            time.sleep(0.02)
            my_bar.progress(percent_complete, text=progress_text)

        prediction = model.predict(input_df)[0]

        # Show result with colors and emojis
        if prediction == 1:
            st.markdown("<h2 style='color: #28a745;'>✅ Likely to get funded! 🌟</h2>", unsafe_allow_html=True)
            st.balloons()
        else:
            st.markdown("<h2 style='color: #dc3545;'>❌ Unlikely to get funded this time. 😞</h2>", unsafe_allow_html=True)
            st.snow()

        # Add some personalized feedback
        if ask_amount > 500000:
            st.info("💡 Pro Tip: Asking for large amounts can sometimes scare investors. Consider breaking your funding rounds into smaller chunks.")
        else:
            st.info("👍 Great funding request! Keep it realistic and achievable.")

        if len(pitch_text) < 100:
            st.warning("✍️ Your pitch is quite short. Try adding more details to convince investors!")

        st.markdown("---")
        st.write("""
        ### How this works
        - I analyze your **pitch text**, **funding ask**, and **industry** using a machine learning model.
        - The prediction is based on historical funding data and patterns.
        - Use this feedback to polish your pitch and funding strategy.
        """)

st.markdown("<footer style='text-align:center; margin-top: 2rem;'>Made with ❤️ by Aarushi Tandon</footer>", unsafe_allow_html=True)
