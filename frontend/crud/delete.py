import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000" 


def delete_movie():
    st.subheader("Delete Movie")
    response = requests.get(f"{BASE_URL}", params={"user_id": st.session_state.user_id})
    if response.status_code == 200:
        all_movies = response.json()

        if all_movies:
            movie_title = st.selectbox("Select Movie Name To Delete", [movie["title"] for movie in all_movies])
            selected_movie = next((movie for movie in all_movies if  movie["title"] == movie_title), None)

            if st.button(f"Delete Movie {selected_movie['title']}"):
                movie_id = selected_movie["id"]
                delete_response = requests.delete(f"{BASE_URL}/{movie_id}")

                if delete_response.status_code == 200:
                    st.success("Movie Deleted Successfully!")
                else:
                    st.error(f"Failed To Delete Movie!")
        else:
            st.info("No Movie Available To Delete")