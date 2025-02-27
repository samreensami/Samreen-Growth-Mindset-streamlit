import streamlit as st 
import pandas as pd

st.set_page_config(page_title="Growth Mindset project", page_icon="❅")

st.title("Growth Mindset Challenge:Web App With Streamlit ")
st.write("Embrace challenges, learn from them, and grow through them...!")

# Quote Section
st.header("⏳ Welcome to your Growth Mindset journey!")
st.write("Success is not about luck; it's about learning, adapting, and never giving up.")

# User Challenge Input
user_input = st.text_input("Describe a challenge you are facing and how you are going to overcome it:")

if user_input:
    st.success(f"Thanks for sharing {user_input} ...!")
else:
    st.warning("Tell us about your challenges to get started...!")

# Reflection Section
st.header("📝 Reflect On Your Learning")
reflection = st.text_area("Enter your reflection:")

if reflection:
    st.success(f"Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on your learning is important. Share your difficulties...!")

# Achievement Section
st.header("🏆 Share Your Achievements")
achievement = st.text_input("Share something you have accomplished:")

if achievement:
    st.success(f"Thanks for sharing {achievement}...!")
else:
    st.info("Share your achievements and successes...!")

# Footer
st.write("---")
st.write("🎉 Keep learning and keep growing...! 🎉")
st.write("🥰 Created by **SAMREEN SAMI** | Roll No: **442750** | Lead Teacher: **Hamzah Syed** 🥰")
