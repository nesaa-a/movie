import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000" 


def update_movie():
    st.subheader("Update Movie")
    response = requests.get(f"{BASE_URL}", params={"user_id": st.session_state.user_id})

    if response.status_code == 200:
        movies = response.json()

        if movies:
            movie_title = st.selectbox("Select Movie To Update", [movie["title"] for movie in movies])
            selected_movie = next((movie for movie in movies if movie["title"] == movie_title))

            if selected_movie:
                title = st.text_input("Movie Title", value=selected_movie["title"])
                category = st.text_input("Category", value=selected_movie["category"])
                release_year = st.number_input("Release Year", min_value=1900, max_value=2025, step=1, value=selected_movie["release_year"])
                description = st.text_area("Description", value=selected_movie["description"])
                
                if st.button("Update Movie"):
                    json = {
                        "title": title,
                        "category": category,
                        "release_year": release_year,
                        "description": description
                    }

                    update_response = requests.put(f"{BASE_URL}/{selected_movie['id']}", json=json)

                    if update_response.status_code == 200:
                        st.success("Movie Updated Successfully!")
                    else:
                        st.error("Failed To update Movie")
        else:
            st.info("No Movie Available To Update.")

