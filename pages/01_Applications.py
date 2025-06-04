import streamlit as st

st.set_page_config(page_title="Applications - Club Multiverse SL", layout="wide")
st.title("📝 Club Applications")
st.write("This is where club application forms or information will go.")

# Iframe for the website
website_url = "https://forms.gle/31gxmvVy2824wKzF9"
st.components.v1.iframe(website_url, height=1650, scrolling=True)

# Iframe for the website
website_url = "https://forms.gle/Q3MmH1DCzpR5Ps729"
st.components.v1.iframe(website_url, height=1650, scrolling=True)