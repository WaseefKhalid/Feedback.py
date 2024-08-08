
import streamlit as st
import pandas as pd
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import base64

# Function to send email with the CSV attachment using smtplib
def send_email(subject, body, to_email, from_email, from_password, file_path):
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Open the file to be sent
    with open(file_path, "rb") as attachment:
        # instance of MIMEBase and named as p
        part = MIMEBase('application', 'octet-stream')
        # To change the payload into encoded form
        part.set_payload((attachment).read())
        # encode into base64
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(file_path)}")

        # attach the instance 'part' to instance 'msg'
        msg.attach(part)

    try:
        # Creates SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Login with mail_id and password
        server.login(from_email, from_password)

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        server.sendmail(from_email, to_email, text)
        server.quit()

        return "Email sent successfully!"

    except Exception as e:
        return str(e)

# Set the page config at the very beginning
st.set_page_config(page_title="QHPC-UOL Cricket Academy Feedback", layout="wide")

# Adding QHPC-UOL logo
st.image("https://upload.wikimedia.org/wikipedia/en/2/2e/Lahore_Qalandars_logo.png", width=200)

# Streamlit app
st.markdown("### Created by Waseef Khalid")
st.title("QHPC-UOL Cricket Academy Feedback")

# Feedback details
st.subheader("Feedback Details")
date = st.date_input("Date", value=datetime.date.today())
name = st.text_input("Your Name")
relation = st.selectbox("Relation to Academy", ["Student", "Parent"])

# Coach feedback section
st.subheader("Coach Feedback")
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
feedback_data = {"Question": questions, "Rating": []}

for i, question in enumerate(questions):
    st.write(f"**{question}**")
    rating = st.radio(f"Rating for {question}", ratings, key=f"rating_{i}", horizontal=True)
    feedback_data["Rating"].append(rating)

# Further comments
st.subheader("Further Comments")
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
    email_status = send_email(
        subject="QHPC-UOL Cricket Academy Feedback",
        body="Please find the attached feedback report.",
        to_email="waseefkhalid481@gmail.com",
        from_email="your_email@example.com",  # Replace with your email
        from_password="your_password",  # Replace with your email password
        file_path=csv_file
    )

    st.success(email_status)

if st.button("Export to CSV"):
    df = pd.DataFrame(feedback_data)
    df.to_csv("cricket_academy_feedback.csv", index=False)
    st.success("Feedback exported to CSV successfully!")
