import streamlit as st
import json
import random

# --- CONFIG ---
st.set_page_config(page_title="P3 Mastery Hub", page_icon="🌟")

# --- LOAD DATA ---
@st.cache_data
def load_questions():
    try:
        with open('questions.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"prepositions": [], "editing": [], "cloze": []}

DATA = load_questions()

# --- INITIALIZE SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = 'start'
if 'lives' not in st.session_state:
    st.session_state.lives = 3
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_idx' not in st.session_state:
    st.session_state.current_idx = 0

# --- FUNCTIONS ---
def start_game(category):
    # Pick the category and shuffle questions to ensure variety
    questions = DATA.get(category, [])
    random.shuffle(questions)
    st.session_state.questions = questions
    st.session_state.mode = category
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.lives = 3
    st.session_state.page = 'game'

def check_answer(user_val, correct_val):
    if user_val.lower().strip() == correct_val.lower().strip():
        st.session_state.score += 1
        st.toast("⭐ Correct!", icon="✅")
    else:
        st.session_state.lives -= 1
        st.error(f"❌ Incorrect! The right answer is: {correct_val}")
    
    st.session_state.current_idx += 1
    if st.session_state.lives <= 0 or st.session_state.current_idx >= len(st.session_state.questions):
        st.session_state.page = 'result'

# --- PAGE ROUTING ---
if st.session_state.page == 'start':
    st.title("🌟 P3 Mastery Elite")
    st.markdown("### Choose your training module:")
    
    col1, col2, col3 = st.columns(3)
    if col1.button("📍 Prepositions"): start_game("prepositions")
    if col2.button("📖 Grammar Cloze"): start_game("cloze")
    if col3.button("✍️ Typing Challenge"): start_game("editing")

elif st.session_state.page == 'game':
    q = st.session_state.questions[st.session_state.current_idx]
    
    st.header(f"Mode: {st.session_state.mode.title()}")
    st.write(f"**Lives:** {'❤️' * st.session_state.lives} | **Score:** {st.session_state.score}")
    st.progress(st.session_state.current_idx / len(st.session_state.questions))
    
    st.divider()
    st.write(f"### Question {st.session_state.current_idx + 1}")
    st.write(f"## {q['q']}")
    
    # Logic for Multiple Choice vs Typing
    if "options" in q:
        # Multiple Choice Layout
        shuffled_options = q['options'].copy()
        random.shuffle(shuffled_options)
        
        c1, c2 = st.columns(2)
        for i, opt in enumerate(shuffled_options):
            target_col = c1 if i % 2 == 0 else c2
            if target_col.button(opt, key=f"opt_{i}", use_container_width=True):
                check_answer(opt, q['a'])
                st.rerun()
    else:
        # Typing Mode Layout
        user_input = st.text_input("Type the correct word here:", key="typing_box").strip()
        if st.button("Submit Answer", use_container_width=True):
            if user_input:
                check_answer(user_input, q['a'])
                st.rerun()
            else:
                st.warning("Please type something!")

elif st.session_state.page == 'result':
    st.title("🏁 Challenge Result")
    
    if st.session_state.lives <= 0:
        st.error("GAME OVER")
        st.write("You ran out of lives! Time for a quick review.")
    else:
        st.balloons()
        st.success("WELL DONE!")
        
    st.metric("Final Score", f"{st.session_state.score}/{len(st.session_state.questions)}")
    
    if st.button("Back to Main Menu"):
        st.session_state.page = 'start'
        st.rerun()
