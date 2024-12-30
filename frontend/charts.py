import streamlit as st
import requests
import pandas as pd

BASE_URL = "http://127.0.0.1:8000"

def view_report():
    st.subheader("Movies Report")
    if st.button("Generate Report"):
        response = requests.get(f"{BASE_URL}/report", params={"user_id": st.session_state.user_id})
        if response.status_code == 200:
            report = response.json().get("report", {})
            st.write("Movies by Category:")

            # Convert report dictionary to DataFrame for category visualization
            if report:
                df_category = pd.DataFrame(list(report.items()), columns=["Category", "Count"])

                # Generate Bar Chart for categories
                st.bar_chart(df_category.set_index("Category"))
            else:
                st.warning("No movies found for this user.")

            # Additional chart for release year
            st.write("Movies by Release Year:")
            response_movies = requests.get(f"{BASE_URL}/", params={"user_id": st.session_state.user_id})
            if response_movies.status_code == 200:
                movies = response_movies.json()
                if movies:
                    df_movies = pd.DataFrame(movies)

                    # Group by release_year and create a chart
                    release_year_count = df_movies.groupby("release_year").size().reset_index(name="Count")
                    release_year_count = release_year_count.sort_values("release_year")

                    st.bar_chart(release_year_count.set_index("release_year"))
                else:
                    st.warning("No movies found for this user.")
            else:
                st.error("Failed to fetch movies for release year chart.")
        else:
            st.error("Failed to generate report.")
