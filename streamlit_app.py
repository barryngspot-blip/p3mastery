import streamlit as st
import random

# --- DATASET ---
# Replicated from your previous mastery lists
DATA = {
    "Prepositions": [
        {"q": "The athlete sprinted _____ the finish line.", "options": ["across", "through", "over", "along"], "a": "across"},
        {"q": "The map was tucked _____ the pages.", "options": ["between", "among", "inside", "within"], "a": "between"},
        {"q": "Jude practiced his footwork _____ sunset.", "options": ["until", "at", "during", "since"], "a": "until"}
    ],
    "Editing (Typing)": [
        {"q": "Fix the misspelled word: 'She wore beautiful JEWELRY.'", "a": "jewellery"},
        {"q": "Fix the misspelled word: 'The LION was very FEROSIOUS.'", "a": "ferocious"},
        {"q": "Fix the misspelled word: 'We stood in a long QUENE.'", "a": "queue"}
    ],
    "Grammar Cloze": [
        {"q": "The old art _____ was quiet.", "options": ["gallery", "museum", "studio", "hall"], "a": "gallery"},
        {"q": "Jude stepped _____ the room.", "options": ["into", "onto", "to", "at"], "a": "into"}
    ]
}

# --- SESSION STATE INITIALIZATION ---
if 'page' not in st.session_state:
    st.session_state.page = 'start'
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'lives' not in st.session_state:
    st.session_state.lives = 3
if 'current_idx' not in st.session_state:
    st.session_state.current_idx = 0

# --- FUNCTIONS ---
def start_game(mode):
    st.session_state.mode = mode
    st.session_state.questions = random.sample(DATA[mode], len(DATA[mode]))
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.lives = 3
    st.session_state.page = 'game'

def check_answer(user_ans, correct_ans):
    if user_ans.lower().strip() == correct_ans.lower():
        st.session_state.score += 1
        st.success("⭐ Correct!")
    else:
        st.session_state.lives -= 1
        st.error(f"❌ Wrong! The correct answer was: {correct_ans}")
    
    st.session_state.current_idx += 1
    if st.session_state.lives <= 0 or st.session_state.current_idx >= len(st.session_state.questions):
        st.session_state.page = 'result'

# --- UI LAYOUT ---
if st.session_state.page == 'start':
    st.title("🌟 P3 Mastery Elite")
    st.write("Select your training module:")
    if st.button("📍 Prepositions"): start_game("Prepositions")
    if st.button("📖 Grammar Cloze"): start_game("Grammar Cloze")
    if st.button("✍️ Editing (Typing Challenge)"): start_game("Editing (Typing)")

elif st.session_state.page == 'game':
    q = st.session_state.questions[st.session_state.current_idx]
    
    st.subheader(f"Mode: {st.session_state.mode}")
    st.write(f"Lives: {'❤️' * st.session_state.lives}")
    st.progress(st.session_state.current_idx / len(st.session_state.questions))
    
    st.write(f"### {q['q']}")
    
    if "options" in q:
        # Multiple Choice
        cols = st.columns(2)
        for i, opt in enumerate(q['options']):
            if cols[i % 2].button(opt, key=f"btn_{i}"):
                check_answer(opt, q['a'])
                st.rerun()
    else:
        # Typing Mode
        user_input = st.text_input("Type your answer:", key="type_box")
        if st.button("Submit"):
            check_answer(user_input, q['a'])
            st.rerun()

elif st.session_state.page == 'result':
    st.balloons()
    st.title("Challenge Complete!")
    st.metric("Final Score", f"{st.session_state.score}/{len(st.session_state.questions)}")
    if st.button("Back to Menu"):
        st.session_state.page = 'start'
        st.rerun()
