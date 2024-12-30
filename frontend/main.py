import streamlit as st
import pandas as pd
from charts import view_report
from auth.logout import logout
from auth.login import login
from home import home
from crud import add, update, delete
import os
import base64

current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, "logo.png")


def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


def main_app():
    st.title("Movies Managment 🎥")
    st.markdown("---")
    if os.path.exists(logo_path):
        logo_base64 = get_image_as_base64(logo_path)
        logo_html = f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100px; margin-bottom: 50px;">
            <img src="data:image/png;base64,{logo_base64}" style="max-width: 100%; height: auto; width: 300px;">
        </div>
        """
        with st.sidebar:
            st.markdown(logo_html, unsafe_allow_html=True)
      
    menu = ["Home", "Add Movie", "Update Movie", "Delete Movie", "Charts", "Logout"]
    choose_menu = st.sidebar.selectbox("Menu", menu)

    if choose_menu == "Home":
        home()

    elif choose_menu == "Add Movie":
        add.add_movie()
    
    elif choose_menu == "Update Movie":
        update.update_movie()
    
    elif choose_menu == "Delete Movie":
        delete.delete_movie()

    elif choose_menu == "Charts":
        view_report()
    
    elif choose_menu == "Logout":
        logout()
