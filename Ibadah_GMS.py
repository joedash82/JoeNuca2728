!pip install matplotlib
!pip install pandas
!pip install streamlit


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize or load data
if "data" not in st.session_state:
    st.session_state.data = {
        "Week": [],
        "Service": [],
        "Attendance": [],
        "New Members": []
    }

# Title
st.title("Church Service Attendance Tracker")

# User input for the week
week = st.text_input("Enter the week (e.g., Week 1, Week 2):", "Week 1", key="week_input")

# Define available services
services = [
    "Ibadah Umum 1",
    "Ibadah Umum 2",
    "Ibadah Umum 3",
    "Ibadah AOG Youth 1",
    "Ibadah AOG Youth 2",
    "Ibadah Eaglekids 1",
    "Ibadah Eaglekids 2",
    "Ibadah Eaglekids 3"
]

# Input form for attendance data
st.header("Input Attendance Data")
with st.form("attendance_form"):
    for service in services:
        st.subheader(service)
        attendance = st.number_input(f"Attendance for {service}:", min_value=0, value=0, step=1, key=f"attendance_{service}")
        new_members = st.number_input(f"New Members for {service}:", min_value=0, value=0, step=1, key=f"new_members_{service}")

        # Append data to session state
        st.session_state.data["Week"].append(week)
        st.session_state.data["Service"].append(service)
        st.session_state.data["Attendance"].append(attendance)
        st.session_state.data["New Members"].append(new_members)

    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("Data submitted successfully!")

# Convert session state data to a DataFrame
data_df = pd.DataFrame(st.session_state.data)

# Display the data table
st.header("Attendance Data")
st.dataframe(data_df)

# Plot data for each service
st.header("Weekly Attendance Trends")
selected_service = st.selectbox("Select a Service to View Trends:", services, key="service_select")

if selected_service:
    # Filter data for the selected service
    service_data = data_df[data_df["Service"] == selected_service]

    # Plot attendance trends
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(service_data["Week"], service_data["Attendance"], marker="o", label="Attendance")
    ax.plot(service_data["Week"], service_data["New Members"], marker="x", label="New Members")
    
    ax.set_title(f"Attendance Trends for {selected_service}")
    ax.set_xlabel("Week")
    ax.set_ylabel("Count")
    ax.legend()

    st.pyplot(fig)
