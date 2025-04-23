
import streamlit as st
# to align center
# style_heading = 'text-align: center'
# st.markdown(f"<h1 style='{style_heading}'>My First Streamlit Growth Mindset App🧠</h1>", unsafe_allow_html=True)


st.set_page_config(page_title="Growth Mindset", page_icon="🎯", layout="wide")
style_heading = 'text-align: center ; color: orange; font-size: 60px; font-weight: bold;'
st.markdown(f"<h1 style='{style_heading}'>My First Streamlit Growth Mindset App🧠</h1>", unsafe_allow_html=True)
st.header("Step Ahead: Embrace the Growth Mindset!")
st.write("Welcome to the Growth Mindset App! This app is designed to help you develop a growth mindset,  Let's get started on this journey together!")
st.header("What is a Growth Mindset?")
st.write("""A growth mindset is the standpoint that abilities and intelligence can be developed through dedication, hard work, and perseverance. It fosters a love for learning and resilience, essential for great accomplishment...
           
                 In contrast, a fixed mindset is the belief that abilities are static and unchangeable. This app will help you cultivate a growth mindset by providing daily challenges, resources, and tracking your progress""")

challanges = st.selectbox("Select a challenge to get started", ["Embrace Challenges", "Learn from Criticism", "Celebrate Others' Success", "Practice Persistence", "Embrace Failure"])       
if challanges == "Embrace Challenges":
    st.success("Take on a task you've been avoiding. Break it down into smaller steps and start with the first one.") 
elif challanges == "Learn from Criticism":
    st.success("Ask for feedback on a recent project or task. Focus on how you can use the feedback to improve.") 
elif challanges == "Celebrate Others' Success":
    st.success("Identify someone who has achieved something great. Reflect on how their success can inspire you.")    
elif challanges == "Practice Persistence":
    st.success("Set a small goal for today and commit to achieving it, no matter the obstacles.") 
elif challanges == "Embrace Failure":
    st.success("Reflect on a recent failure. Write down three lessons you learned from this experience.") 
st.write("Reflect on this challenge (optional):")
reflection = st.text_area("Reflect on this challenge (optional):", key="reflection")    
if reflection:
    st.success("Great reflection! Keep up the good work.")
st.header("Your Progress") 
                         
st.write("You have completed challenge. Keep up the great work!")



    
    







