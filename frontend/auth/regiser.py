import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

def register():
  st.subheader("Register")
  username = st.text_input("Choose a Username", placeholder="Choose a Username...")
  password = st.text_input("Choose a Username", placeholder="Choose a Username...", type="password")
  if st.button("Register"):
    response = requests.post(f"{BASE_URL}/auth/register", json={"username": username, "password": password})

    if response.status_code == 200:
      st.success("Registration was successful! Please log in.")
    else:
      st.error(f"Registration failed. Try a different username {response.text}")
