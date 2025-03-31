import streamlit as st
import requests
import pandas as pd

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000"

st.title("Biodata")

# Input form
with st.form("user_form"):
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=1, step=1)
    submit = st.form_submit_button("Submit")

# When form is submitted, send data to FastAPI
if submit and name and age:
    response = requests.post(f"{API_URL}/add_user/", json={"name": name, "age": age})
    if response.status_code == 200:
        st.success("User added successfully!")
    else:
        st.error("Error adding user.")

# Fetch and display logged users
st.subheader("Logged Users:")
users_response = requests.get(f"{API_URL}/get_users/")
if users_response.status_code == 200:
    users_data = users_response.json()
    if users_data:
        df = pd.DataFrame(users_data)
        st.table(df)  # Display data as a table
    else:
        st.write("No users logged yet.")
