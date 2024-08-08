# Feedback.py
import streamlit as st
import pandas as pd
import datetime

# Streamlit app
st.set_page_config(page_title="QHPC-UOL Daily Session Activity Report", layout="wide")
st.title("QHPC-UOL Daily Session Activity Report")

# Session details
col1, col2, col3, col4 = st.columns(4)
with col1:
    session_no = st.text_input("Session No.")
with col2:
    date = st.date_input("Date", value=datetime.date.today())
with col3:
    net_no = st.text_input("Net No.")
with col4:
    astro_no = st.text_input("Astro No.")

coach_name = st.text_input("Coach Name")

st.subheader("Player Details")
player_data = {
    "Roll No": [],
    "Student Name": [],
    "Speciality": [],
    "Attendance": [],
    "Nature": [],
    "Ball Played": [],
    "Specific Drills/Skill Work": [],
    "Areas of Improvement": [],
    "Key Strength": [],
    "Remarks": []
}

num_players = st.number_input("Number of Players", min_value=1, step=1)

for i in range(num_players):
    st.markdown(f"**Player {i + 1}**")
    col1, col2 = st.columns(2)
    with col1:
        player_data["Roll No"].append(st.text_input(f"Roll No. {i + 1}", key=f"roll_no_{i}"))
    with col2:
        player_data["Student Name"].append(st.text_input(f"Student Name {i + 1}", key=f"student_name_{i}"))
        
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        player_data["Speciality"].append(st.selectbox(f"Speciality {i + 1}", ["Batter", "Bowler", "All Rounder"], key=f"speciality_{i}"))
    with col2:
        player_data["Attendance"].append(st.selectbox(f"Attendance {i + 1}", ["Present", "Absent"], key=f"attendance_{i}"))
    with col3:
        player_data["Nature"].append(st.selectbox(f"Nature {i + 1}", ["Attack", "Defend"], key=f"nature_{i}"))
    with col4:
        player_data["Ball Played"].append(st.selectbox(f"Ball Played {i + 1}", ["Astro Turf", "Cement"], key=f"ball_played_{i}"))
    with col5:
        player_data["Specific Drills/Skill Work"].append(st.text_input(f"Specific Drills/Skill Work {i + 1}", key=f"specific_drills_{i}"))
    with col6:
        player_data["Remarks"].append(st.text_input(f"Remarks {i + 1}", key=f"remarks_{i}"))

    col1, col2, col3 = st.columns(3)
    with col1:
        player_data["Areas of Improvement"].append(st.text_input(f"Areas of Improvement {i + 1}", key=f"areas_of_improvement_{i}"))
    with col2:
        player_data["Key Strength"].append(st.text_input(f"Key Strength {i + 1}", key=f"key_strength_{i}"))
    with col3:
        player_data["Remarks"].append(st.text_input(f"Remarks {i + 1}", key=f"remarks_{i+num_players}"))

if st.button("Submit"):
    df = pd.DataFrame(player_data)
    st.write(df)
    
    # Save dataframe to CSV
    csv_file = "session_activity_report.csv"
    df.to_csv(csv_file, index=False)
    st.success("Data submitted and saved to CSV successfully!")

if st.button("Export to CSV"):
    df = pd.DataFrame(player_data)
    df.to_csv("session_activity_report.csv", index=False)
    st.success("Data exported to CSV successfully!")
