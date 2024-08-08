# Feedback.py
import streamlit as st
import pandas as pd
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Function to send email with the CSV attachment
def send_email(file_path, recipient_email):
    from_email = "your_email@example.com"  # Replace with your email
    from_password = "your_password"        # Replace with your email password

    subject = "QHPC-UOL Cricket Academy Feedback"
    body = "Please find the attached feedback report."

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    attachment = open(file_path, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(file_path)}")
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, recipient_email, text)
    server.quit()

# Set the page config at the very beginning
st.set_page_config(page_title="QHPC-UOL Cricket Academy Feedback", layout="wide")

# QHPC-UOL theme colors
primary_color = "#FF0000"  # Red color for primary elements
secondary_color = "#FFFFFF"  # White color for secondary elements
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

# Adding QHPC-UOL logo
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

# Feedback questions
questions = [
    "I enjoyed the training session today",
    "I learnt something new today",
    "The coach/teacher made the session interesting",
    "The coach/teacher explained things clearly",
    "I knew what I needed to develop today",
    "The training focused on relevant skills",
    "The training session was well planned",
    "I would want to do this training session again",
    "I would recommend this training session to others"
]
ratings = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
feedback_data = {"Question": questions, "Rating": [], "Comments": []}

for i, question in enumerate(questions):
    st.write(f"#### {question}")
    rating = st.selectbox(f"Rating for {question}", ratings, key=f"rating_{i}")
    feedback_data["Rating"].append(rating)

# Further comments
st.write("### Further Comments")
improvement_comments = st.text_area("How could the training session be improved?")
positive_comments = st.text_area("What did the coach/teacher do well?")
additional_comments = st.text_area("If you have any additional comments, please use the space below:")

if st.button("Submit Feedback"):
    df = pd.DataFrame(feedback_data)
    st.write(df)

    # Save dataframe to CSV
    csv_file = "cricket_academy_feedback.csv"
    df.to_csv(csv_file, index=False)

    # Save comments to a separate text file
    comments_file = "comments.txt"
    with open(comments_file, "w") as file:
        file.write(f"Improvement Comments:\n{improvement_comments}\n\n")
        file.write(f"Positive Comments:\n{positive_comments}\n\n")
        file.write(f"Additional Comments:\n{additional_comments}\n")

    # Send email with CSV and comments
    send_email(csv_file, "waseefkhalid481@gmail.com")
    send_email(comments_file, "waseefkhalid481@gmail.com")

    st.success("Feedback submitted and sent to email successfully!")

if st.button("Export to CSV"):
    df = pd.DataFrame(feedback_data)
    df.to_csv("cricket_academy_feedback.csv", index=False)
    st.success("Feedback exported to CSV successfully!")
