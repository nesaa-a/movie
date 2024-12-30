import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000" 


def add_movie():
    st.subheader("Add Movie")
    title = st.text_input("Movie Title")
    category = st.text_input("Category")
    release_year = st.number_input("Release Year", min_value=1900, max_value=2025, step=1)
    description = st.text_area("Description")
    if st.button("Add Movie"):
        response = requests.post(
            f"{BASE_URL}",
            json={
                "user_id": st.session_state.user_id,
                "title": title,
                "category": category,
                "release_year": release_year,
                "description": description,
            },
        )
        if response.status_code == 200:
            st.success("Movie added successfully!")
        else:
            st.error(f"Failed to add movie. Error: {response.json()}")
