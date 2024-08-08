import streamlit as st
import pandas as pd
import os

# Streamlit app
st.title("QHPC-UOL Daily Session Activity Report")

session_no = st.text_input("Session No.")
date = st.date_input("Date")
net_no = st.text_input("Net No.")
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
    st.write(f"Player {i + 1}")
    player_data["Roll No"].append(st.text_input(f"Roll No. {i + 1}"))
    player_data["Student Name"].append(st.text_input(f"Student Name {i + 1}"))
    player_data["Speciality"].append(st.selectbox(f"Speciality {i + 1}", ["Batter", "Bowler", "All Rounder"]))
    player_data["Attendance"].append(st.selectbox(f"Attendance {i + 1}", ["Present", "Absent"]))
    player_data["Nature"].append(st.selectbox(f"Nature {i + 1}", ["Attack", "Defend"]))
    player_data["Ball Played"].append(st.selectbox(f"Ball Played {i + 1}", ["Astro Turf", "Cement"]))
    player_data["Specific Drills/Skill Work"].append(st.text_input(f"Specific Drills/Skill Work {i + 1}"))
    player_data["Areas of Improvement"].append(st.text_input(f"Areas of Improvement {i + 1}"))
    player_data["Key Strength"].append(st.text_input(f"Key Strength {i + 1}"))
    player_data["Remarks"].append(st.text_input(f"Remarks {i + 1}"))

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
