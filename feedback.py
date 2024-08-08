import streamlit as st
import pandas as pd

# Set up page configuration
st.set_page_config(page_title="QHPC-UOL Daily Session Activity Report", page_icon="🏏")

# App Title
st.title("QHPC-UOL Daily Session Activity Report")

# Session Details
with st.form(key='session_form'):
    session_no = st.text_input("Session No.", placeholder="Enter session number")
    date = st.date_input("Date")
    net_no = st.text_input("Net No.", placeholder="Enter net number")
    astro_no = st.text_input("Astro No.", placeholder="Enter astro number")
    coach_name = st.text_input("Coach Name", placeholder="Enter coach's name")

    st.subheader("Player Details")
    num_players = st.number_input("Number of Players", min_value=1, step=1)

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

    for i in range(num_players):
        st.write(f"### Player {i + 1}")
        col1, col2 = st.columns(2)
        with col1:
            player_data["Roll No"].append(st.text_input(f"Roll No. {i + 1}"))
            player_data["Student Name"].append(st.text_input(f"Student Name {i + 1}"))
            player_data["Speciality"].append(st.selectbox(f"Speciality {i + 1}", ["Batter", "Bowler", "All Rounder"]))
            player_data["Attendance"].append(st.selectbox(f"Attendance {i + 1}", ["Present", "Absent"]))
        with col2:
            if player_data["Attendance"][-1] == "Present":
                player_data["Nature"].append(st.selectbox(f"Nature {i + 1}", ["Attack", "Defend"]))
                player_data["Ball Played"].append(st.selectbox(f"Ball Played {i + 1}", ["Astro Turf", "Cement"]))
                player_data["Specific Drills/Skill Work"].append(st.text_input(f"Specific Drills/Skill Work {i + 1}"))
                player_data["Areas of Improvement"].append(st.text_input(f"Areas of Improvement {i + 1}"))
                player_data["Key Strength"].append(st.text_input(f"Key Strength {i + 1}"))
                player_data["Remarks"].append(st.text_input(f"Remarks {i + 1}"))
            else:
                player_data["Nature"].append(None)
                player_data["Ball Played"].append(None)
                player_data["Specific Drills/Skill Work"].append(None)
                player_data["Areas of Improvement"].append(None)
                player_data["Key Strength"].append(None)
                player_data["Remarks"].append(None)
    
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    df = pd.DataFrame(player_data)
    st.write("### Submitted Data")
    st.dataframe(df)
    
    # Save DataFrame to CSV
    csv_file = f"session_activity_report_{date}.csv"
    df.to_csv(csv_file, index=False)
    st.success(f"Data submitted and saved to CSV as {csv_file} successfully!")

# Export CSV Option
if st.button("Export to CSV"):
    df = pd.DataFrame(player_data)
    if not df.empty:
        df.to_csv(csv_file, index=False)
        st.success(f"Data exported to CSV as {csv_file} successfully!")
    else:
        st.warning("No data to export!")
