import streamlit as st

st.set_page_config(page_title="Calendar - Club Multiverse SL", layout="wide")
st.title("🗓️ Club Calendar")
st.write("Upcoming events and important dates will be displayed here.")
# Add your content for the calendar here (e.g., embed a Google Calendar, or list events)

# Iframe for the website
website_url = "https://clubmultiversesl.com/schedule/"
st.components.v1.iframe(website_url, height=1500, scrolling=False)
our content for the calendar here (e.g., embed a Google Calendar, or list events)