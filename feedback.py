import streamlit as st
import pandas as pd
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Function to initialize the Google Sheets connection
def init_gsheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your-service-account-file.json", scope)
    client = gspread.authorize(creds)
    return client.open("Your Google Sheet Name").sheet1  # Replace with your Google Sheet name

# Function to insert data into Google Sheets
def insert_feedback(sheet, data_tuple):
    sheet.append_row(data_tuple)

# Initialize Google Sheets
sheet = init_gsheet()

# Set the page config at the very beginning
st.set_page_config(page_title="QHPC-UOL Cricket Academy Feedback", layout="wide")

# Adding QHPC-UOL logo
st.image("https://upload.wikimedia.org/wikipedia/en/2/2e/Lahore_Qalandars_logo.png", width=200)

# Streamlit app
st.markdown("### Created by Waseef Khalid")
st.title("QHPC-UOL Cricket Academy Feedback")

# Feedback details
with st.form(key='feedback_form'):
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

    # Submit button
    submit_button = st.form_submit_button(label='Submit Feedback')

if submit_button:
    data_tuple = [str(date), name, relation, coach_name,
                  feedback_data['Question'][0], feedback_data['Rating'][0],
                  feedback_data['Question'][1], feedback_data['Rating'][1],
                  feedback_data['Question'][2], feedback_data['Rating'][2],
                  feedback_data['Question'][3], feedback_data['Rating'][3],
                  feedback_data['Question'][4], feedback_data['Rating'][4],
                  feedback_data['Question'][5], feedback_data['Rating'][5],
                  feedback_data['Question'][6], feedback_data['Rating'][6],
                  feedback_data['Question'][7], feedback_data['Rating'][7],
                  feedback_data['Question'][8], feedback_data['Rating'][8],
                  improvement_comments, positive_comments, additional_comments]
    insert_feedback(sheet, data_tuple)
    st.success("Feedback submitted successfully!")

    # Optional: Display the feedback data
    df = pd.DataFrame(feedback_data)
    st.write(df)

# Optional: Export feedback data to CSV
if st.button("Export to CSV"):
    rows = sheet.get_all_values()
    df = pd.DataFrame(rows, columns=['Date', 'Name', 'Relation', 'Coach Name',
                                     'Question1', 'Rating1', 'Question2', 'Rating2',
                                     'Question3', 'Rating3', 'Question4', 'Rating4',
                                     'Question5', 'Rating5', 'Question6', 'Rating6',
                                     'Question7', 'Rating7', 'Question8', 'Rating8',
                                     'Question9', 'Rating9', 'Improvement Comments',
                                     'Positive Comments', 'Additional Comments'])
    df.to_csv("all_feedback.csv", index=False)
    st.success("All feedback data exported to CSV successfully!")

