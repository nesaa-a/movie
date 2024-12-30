import streamlit as st
import pandas as pd
import requests

BASE_URL = "http://127.0.0.1:8000"

def home():
  st.subheader(f"Welcome {st.session_state.username.capitalize()}")
  st.write("**Use this application to manage your favorite movies!**")
  st.markdown("---")
  st.subheader("**Movies 🎥**")

  response = requests.get(f"{BASE_URL}", params={"user_id": st.session_state.user_id})
  all_movies = response.json()
  if all_movies:
    movies_df = pd.DataFrame(all_movies)
    if "id" in movies_df.columns and "user_id" in movies_df.columns:
      movies_df = movies_df.drop(columns=["id", "user_id"])
    movies_df.reset_index(drop=True, inplace=True)
    st.dataframe(movies_df, use_container_width=True, hide_index=True)
  else:
    st.info("No Movies Available")
  