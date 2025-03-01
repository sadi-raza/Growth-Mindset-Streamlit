
import streamlit as st
import random
import json
import os
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="Growth Mindset App", page_icon="🧠", layout="wide")

# File to store user data
DATA_FILE = "user_data.json"

# Initialize session state
if 'completed_challenges' not in st.session_state:
    st.session_state.completed_challenges = []

# Load user data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"completed_challenges": []}

# Save user data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# Load data at the start of the session
user_data = load_data()
st.session_state.completed_challenges = user_data["completed_challenges"]

# Challenges data
challenges = [
    {
        "title": "Embrace Challenges",
        "description": "Take on a task you've been avoiding. Break it down into smaller steps and start with the first one.",
    },
    {
        "title": "Learn from Criticism",
        "description": "Ask for feedback on a recent project or task. Focus on how you can use the feedback to improve.",
    },
    {
        "title": "Celebrate Others' Success",
        "description": "Identify someone who has achieved something great. Reflect on how their success can inspire you.",
    },
    {
        "title": "Practice Persistence",
        "description": "Set a small goal for today and commit to achieving it, no matter the obstacles.",
    },
    {
        "title": "Embrace Failure",
        "description": "Reflect on a recent failure. Write down three lessons you learned from this experience.",
    },
]

def get_daily_challenge():
    return random.choice(challenges)

def home():
    st.title("🧠 Growth Mindset App")
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Unlock your potential and overcome challenges with a growth mindset.</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("🤔 What is Growth Mindset?")
        st.info("A growth mindset is the belief that abilities can be developed through dedication and hard work. It creates a love for learning and resilience essential for great accomplishment.")
    
    with col2:
        st.header("🌟 Benefits of Growth Mindset")
        benefits = [
            "Increased motivation and achievement",
            "Better problem-solving skills",
            "Improved self-awareness",
            "Greater resilience in face of setbacks"
        ]
        for benefit in benefits:
            st.success(benefit)

def daily_challenge():
    st.header("🎯 Daily Growth Mindset Challenge")
    challenge = get_daily_challenge()
    
    st.subheader(challenge["title"])
    st.write(challenge["description"])
    
    if st.button("Mark as Completed", key="complete_challenge"):
        if challenge not in st.session_state.completed_challenges:
            st.session_state.completed_challenges.append(challenge)
            save_data({"completed_challenges": st.session_state.completed_challenges})
            st.balloons()
            st.success("Challenge completed! Great job!")
        else:
            st.info("You've already completed this challenge. Great work!")
    
    # Add a reflection input
    reflection = st.text_area("Reflect on this challenge (optional):", key="reflection")
    if reflection:
        st.success("Great reflection! Keep up the good work.")

def progress():
    st.header("📊 Your Progress")
    completed_count = len(st.session_state.completed_challenges)
    st.write(f"You have completed {completed_count} challenges so far. Keep up the great work!")
    
    if completed_count > 0:
        st.subheader("Completed Challenges:")
        for challenge in st.session_state.completed_challenges:
            st.write(f"- {challenge['title']}")
        
        # Create a progress visualization
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = completed_count,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Challenges Completed"},
            gauge = {
                'axis': {'range': [None, 20]},
                'steps': [
                    {'range': [0, 5], 'color': "lightgray"},
                    {'range': [5, 15], 'color': "gray"}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 15}}))
        st.plotly_chart(fig)
    else:
        st.write("Complete your first challenge to start tracking your progress!")

def resources():
    st.header("📚 Growth Mindset Resources")
    st.write("Here are some resources to help you develop and maintain a growth mindset:")
    
    st.subheader("Books")
    books = [
        "'Mindset: The New Psychology of Success' by Carol S. Dweck",
        "'Grit: The Power of Passion and Perseverance' by Angela Duckworth"
    ]
    for book in books:
        st.markdown(f"- {book}")
    
    st.subheader("Videos")
    videos = {
        "The Power of Belief - Mindset and Success": "https://www.youtube.com/watch?v=pN34FNbOKXc",
        "Growth Mindset vs. Fixed Mindset": "https://www.youtube.com/watch?v=KUWn_TJTrnU"
    }
    for title, url in videos.items():
        st.markdown(f"- [{title}]({url})")
    
    st.subheader("Articles")
    articles = {
        "Developing a Growth Mindset with Carol Dweck": "https://fs.blog/carol-dweck-mindset/",
        "10 Ways to Develop a Growth Mindset": "https://www.psychologytoday.com/us/blog/click-here-happiness/201904/15-ways-build-growth-mindset"
    }
    for title, url in articles.items():
        st.markdown(f"- [{title}]({url})")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Daily Challenge", "Progress", "Resources"])
    
    if page == "Home":
        home()
    elif page == "Daily Challenge":
        daily_challenge()
    elif page == "Progress":
        progress()
    elif page == "Resources":
        resources()

if __name__ == "__main__":
    main()




