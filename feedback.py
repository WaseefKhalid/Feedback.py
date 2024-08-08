import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Function to send email
def send_email(subject, body, to_email, file_path):
    # Email credentials
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"
    
    # Create the email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, "plain"))

    # Open the file to be sent
    with open(file_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name=file_path)
        part['Content-Disposition'] = f'attachment; filename="{file_path}"'
        msg.attach(part)

    # Create a secure SSL context and send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())

# Streamlit app
st.title("Send a Message to Receive via Email")

# Input field for the message
message = st.text_area("Enter your message here")

# Button to submit
if st.button("Submit"):
    if message:
        # Create a DataFrame
        df = pd.DataFrame({"Message": [message]})
        
        # Save to CSV
        csv_file = "message.csv"
        df.to_csv(csv_file, index=False)
        
        # Send the email with the CSV attachment
        send_email(
            subject="New Message from Waseef",
            body="Please find the attached message.",
            to_email="your_email@example.com",
            file_path=csv_file
        )
        
        st.success("Message sent successfully!")
    else:
        st.error("Please enter a message.")
