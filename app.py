import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge" )
st.title("Growth Mindset Challenge: Web App with Streamlit")
st.header("Here is your Growth Journey")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential.This AI-powered app helps you build a growth mindset with reflection")

#quote section
st.header("Todays Growth Mindset Quote")
st.write(' "Success is not final, failure is not fatal: it is the courageto continue that counts" ' )

st.header("Whats your Challenge Today")
user_input = st.text_input("Describe your challenge you're facing:")

#condition
if user_input:
    st.success (f"you're facing: {user_input}. Keep pushing forward toward your goal!")
else:
    st.warning("Tell us about your challenge")
    

#reflection
st.header("Reflect your learning")  
reflection = st.text_area("Write your reflection here") 

if reflection:
    st.success(f"Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you to grow! Share your difficulties")

    #achievement
    st.header("Celebrate Your Wins!")
    acheive= st.text_input("Share something you've recently accomplished")
    
    if acheive:
        st.success(f"Amazing! You achieved: {acheive}")
    else:
        st.info("Big or small , every acheivement counts! Share one now")

        #footer
        st.write("- - -")
        st.write("Keep believing in yourself. Growth is a journey, not a destination")
        st.write("Build by Syed Ahsan")
