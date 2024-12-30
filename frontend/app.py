import streamlit as st
import requests
from crud.add import add_movie
from auth.login import login
from auth.regiser import register
from auth.logout import logout
from main import main_app
import os
import base64


BASE_URL = "http://127.0.0.1:8000"

if "user_authenticated" not in st.session_state:
    st.session_state.user_authenticated = False
if "user_id" not in st.session_state:
    st.session_state.user_id = None

current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, "logo.png")


def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


if not st.session_state.user_authenticated:
    if os.path.exists(logo_path):
        logo_base64 = get_image_as_base64(logo_path)
        logo_html = f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100px; margin-bottom: 50px;">
            <img src="data:image/png;base64,{logo_base64}" style="max-width: 100%; height: auto; width: 300px;">
        </div>
        """
        with st.sidebar:
            st.markdown(logo_html, unsafe_allow_html=True)
    st.sidebar.header("Authentication")
    auth_choise = st.sidebar.radio("Choose an option", ["Login", "Register"])
    if auth_choise == "Login":
        login()
    elif auth_choise == "Register":
        register()
else:
    main_app()