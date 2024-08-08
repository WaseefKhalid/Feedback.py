import streamlit as st
import requests
import datetime
import pandas as pd

# Function to submit data to Google Forms
def submit_form(data):
    form_url = "https://docs.google.com/forms/d/e/your-google-form-id/formResponse"
    form_data = {
        "entry.your-entry-id-for-date": data["date"],
        "entry.your-entry-id-for-name": data["name"],
        "entry.your-entry-id-for-relation": data["relation"],
        "entry.your-entry-id-for-coach_name": data["coach_name"],
        "entry.your-entry-id-for-question1": data["question1"],
        "entry.your-entry-id-for-rating1": data["rating1"],
        "entry.your-entry-id-for-question2": data["question2"],
        "entry.your-entry-id-for-rating2": data["rating2"],
        "entry.your-entry-id-for-question3": data["question3"],
        "entry.your-entry-id-for-rating3": data["rating3"],
        "entry.your-entry-id-for-question4": data["question4"],
        "entry.your-entry-id-for-rating4": data["rating4"],
        "entry.your-entry-id-for-question5": data["question5"],
        "entry.your-entry-id-for-rating5": data["rating5"],
        "entry.your-entry-id-for-question6": data["question6"],
        "entry.your-entry-id-for-rating6": data["rating6"],
        "entry.your-entry-id-for-question7": data["question7"],
        "entry.your-entry-id-for-rating7": data["rating7"],
        "entry.your-entry-id-for-question8": data["question8"],
        "entry.your-entry-id-for-rating8": data["rating8"],
        "entry.your-entry-id-for-question9": data["question9"],
        "entry.your-entry-id-for-rating9": data["rating9"],
        "entry.your-entry-id-for-improvement_comments": data["improvement_comments"],
        "entry.your-entry-id-for-positive_comments": data["positive_comments"],
        "entry.your-entry-id-for-additional_comments": data["additional_comments"]
    }
    response = requests.post(form_url, data=form_data)
    return response.status_code

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
    data = {
        "date": str(date),
        "name": name,
        "relation": relation,
        "coach_name": coach_name,
        "question1": questions[0],
        "rating1": feedback_data["Rating"][0],
        "question2": questions[1],
        "rating2": feedback_data["Rating"][1],
        "question3": questions[2],
        "rating3": feedback_data["Rating"][2],
        "question4": questions[3],
        "rating4": feedback_data["Rating"][3],
        "question5": questions[4],
        "rating5": feedback_data["Rating"][4],
        "question6": questions[5],
        "rating6": feedback_data["Rating"][5],
        "question7": questions[6],
        "rating7": feedback_data["Rating"][6],
        "question8": questions[7],
        "rating8": feedback_data["Rating"][7],
        "question9": questions[8],
        "rating9": feedback_data["Rating"][8],
        "improvement_comments": improvement_comments,
        "positive_comments": positive_comments,
        "additional_comments": additional_comments
    }
    status = submit_form(data)
    if status == 200:
        st.success("Feedback submitted successfully!")
    else:
        st.error("There was an error submitting your feedback.")

    # Optional: Display the feedback data
    feedback_display = {
        "Question": questions,
        "Rating": feedback_data["Rating"]
    }
    df = pd.DataFrame(feedback_display)
    st.write(df)

