# Feedback.py
import streamlit as st
import pandas as pd
import datetime

# Set the page config at the very beginning
st.set_page_config(page_title="QHPC-UOL Cricket Academy Feedback", layout="wide")

# Lahore Qalandars theme colors
primary_color = "#FF0000"  # Red color for primary elements
secondary_color = "#000000"  # Black color for secondary elements
background_color = "#90EE90"  # Light green color for background

# Custom CSS for theme
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {background_color};
            color: {secondary_color};
        }}
        .stButton > button {{
            background-color: {primary_color};
            color: {secondary_color};
        }}
        .stTextInput > div > div > input {{
            background-color: {secondary_color};
            color: {background_color};
        }}
        .stSelectbox > div > div > div {{
            background-color: {secondary_color};
            color: {background_color};
        }}
    </style>
    """, unsafe_allow_html=True)

# Adding Lahore Qalandars logo
st.image("https://upload.wikimedia.org/wikipedia/en/2/2e/Lahore_Qalandars_logo.png", width=200)

# Streamlit app
st.title("QHPC-UOL Cricket Academy Feedback")

# Feedback details
st.write("### Feedback Details")
date = st.date_input("Date", value=datetime.date.today())
name = st.text_input("Your Name")
relation = st.selectbox("Relation to Academy", ["Student", "Parent"])

# Coach feedback section
st.write("### Coach Feedback")
coach_name = st.text_input("Coach Name")

ratings = ["Excellent", "Good", "Average", "Poor"]
feedback_data = {
    "Category": ["Knowledge of the game", "Communication skills", "Encouragement and support", "Overall satisfaction"],
    "Rating": [],
    "Comments": []
}

for category in feedback_data["Category"]:
    st.write(f"#### {category}")
    rating = st.selectbox(f"Rating for {category}", ratings, key=f"rating_{category}")
    comment = st.text_area(f"Comments for {category}", key=f"comment_{category}")
    feedback_data["Rating"].append(rating)
    feedback_data["Comments"].append(comment)

if st.button("Submit Feedback"):
    df = pd.DataFrame(feedback_data)
    st.write(df)

    # Save dataframe to CSV
    csv_file = "cricket_academy_feedback.csv"
    df.to_csv(csv_file, index=False)
    st.success("Feedback submitted and saved to CSV successfully!")

if st.button("Export to CSV"):
    df = pd.DataFrame(feedback_data)
    df.to_csv("cricket_academy_feedback.csv", index=False)
    st.success("Feedback exported to CSV successfully!")
