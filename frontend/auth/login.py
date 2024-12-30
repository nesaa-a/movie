import streamlit as st
import requests
import os
import base64


BASE_URL = "http://127.0.0.1:8000"

current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, "logo.png")


def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def login():
  st.subheader("Login")
  if os.path.exists(logo_path):
        logo_base64 = get_image_as_base64(logo_path)
        logo_html = f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100px; margin-bottom: 50px;">
            <img src="data:image/png;base64,{logo_base64}" style="max-width: 100%; height: auto; width: 300px;">
        </div>
        """
        with st.sidebar:
            st.markdown(logo_html, unsafe_allow_html=True)
  username = st.text_input("Username", placeholder="Username")
  password = st.text_input("Password", placeholder="Password", type="password")
  if st.button("Login"):
    response = requests.post(f"{BASE_URL}/auth/login", json={"username": username, "password": password})

    if response.status_code == 200:
      user_data = response.json()
      st.session_state.user_authenticated = True
      st.session_state.user_id = user_data["user_id"]
      st.session_state.username = user_data["username"]
      st.success(f"Welcome Back {st.session_state.username}")
      return
    else:
      st.error("Invalid username or password")
