# Feedback.py
import streamlit as st
import pandas as pd
import datetime

# Set the page config at the very beginning
st.set_page_config(page_title="QHPC-UOL Daily Session Activity Report", layout="wide")

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
st.title("QHPC-UOL Daily Session Activity Report")

# Session details
st.write("### Session Details")
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

st.write("### Player Details")
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
    st.markdown(f"#### Player {i + 1}")
    col1, col2 = st.columns(2)
    with col1:
        player_data["Roll No"].append(st.text_input(f"Roll No.", key=f"roll_no_{i}"))
    with col2:
        player_data["Student Name"].append(st.text_input(f"Student Name", key=f"student_name_{i}"))

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        player_data["Speciality"].append(st.selectbox("Speciality", ["Batter", "Bowler", "All Rounder"], key=f"speciality_{i}"))
    with col2:
        player_data["Attendance"].append(st.selectbox("Attendance", ["Present", "Absent"], key=f"attendance_{i}"))
    with col3:
        player_data["Nature"].append(st.selectbox("Nature", ["Attack", "Defend"], key=f"nature_{i}"))
    with col4:
        player_data["Ball Played"].append(st.selectbox("Ball Played", ["Astro Turf", "Cement"], key=f"ball_played_{i}"))
    with col5:
        player_data["Specific Drills/Skill Work"].append(st.text_input("Specific Drills/Skill Work", key=f"specific_drills_{i}"))
    with col6:
        player_data["Remarks"].append(st.text_input("Remarks", key=f"remarks_{i}"))

    col1, col2, col3 = st.columns(3)
    with col1:
        player_data["Areas of Improvement"].append(st.text_input("Areas of Improvement", key=f"areas_of_improvement_{i}"))
    with col2:
        player_data["Key Strength"].append(st.text_input("Key Strength", key=f"key_strength_{i}"))
    with col3:
        player_data["Remarks"].append(st.text_input("Remarks", key=f"remarks_{i+num_players}"))

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
