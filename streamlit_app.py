import streamlit as st
import random

# --- DATASET ---
# Replicated from your previous mastery lists
DATA = {
      "Prepositions": [
        {"q": "The athlete sprinted _____ the finish line.", "options": ["across", "through", "over", "along"], "a": "across"},
        {"q": "The map was tucked _____ the brittle pages.", "options": ["between", "among", "inside", "within"], "a": "between"},
        {"q": "Jude practiced his footwork _____ sunset.", "options": ["until", "at", "during", "since"], "a": "until"},
        {"q": "The predator remained motionless _____ the tall grass.", "options": ["among", "between", "beside", "inside"], "a": "among"},
        {"q": "The hikers trekked _____ the summit.", "options": ["toward", "onto", "into", "past"], "a": "toward"},
        {"q": "The stream flows _____ the old stone bridge.", "options": ["under", "above", "across", "through"], "a": "under"},
        {"q": "The kite soared high _____ the trees.", "options": ["above", "over", "beyond", "up"], "a": "above"},
        {"q": "At the whistle, the swimmers dived _____ the pool.", "options": ["into", "onto", "in", "to"], "a": "into"},
        {"q": "The ball rolled _____ the goalkeeper and into the net.", "options": ["past", "passed", "by", "over"], "a": "past"},
        {"q": "The group gathered _____ the campfire to stay warm.", "options": ["around", "among", "between", "beside"], "a": "around"},
        {"q": "Keep your elbows _____ the table while eating.", "options": ["off", "of", "from", "at"], "a": "off"},
        {"q": "The plane flew _____ the thick clouds.", "options": ["through", "across", "along", "past"], "a": "through"},
        {"q": "He leaned his bicycle _____ the wooden fence.", "options": ["against", "opposite", "beside", "on"], "a": "against"},
        {"q": "The keys fell _____ the narrow gap in the floorboards.", "options": ["down", "into", "through", "below"], "a": "through"},
        {"q": "We walked _____ the beach as the sun went down.", "options": ["along", "across", "through", "over"], "a": "along"},
        {"q": "The moon appeared _____ the clouds.", "options": ["behind", "between", "under", "below"], "a": "behind"},
        {"q": "The cat jumped _____ the high wall.", "options": ["onto", "into", "at", "to"], "a": "onto"},
        {"q": "The treasure was hidden _____ the two palm trees.", "options": ["between", "among", "beside", "next"], "a": "between"},
        {"q": "He ran _____ the stairs to answer the door.", "options": ["down", "under", "below", "off"], "a": "down"},
        {"q": "The mouse scurried _____ the hole in the wall.", "options": ["into", "onto", "at", "to"], "a": "into"},
        {"q": "We drove _____ the long tunnel.", "options": ["through", "across", "along", "past"], "a": "through"},
        {"q": "The child hid _____ the bed during the game.", "options": ["under", "below", "beneath", "behind"], "a": "under"},
        {"q": "They sat _____ the shade of a large oak tree.", "options": ["in", "under", "below", "on"], "a": "in"},
        {"q": "The spider crawled _____ the ceiling.", "options": ["across", "through", "along", "over"], "a": "across"},
        {"q": "The ferry travels _____ the river every hour.", "options": ["across", "through", "along", "past"], "a": "across"},
        {"q": "He looked _____ the window at the rain.", "options": ["out of", "through", "from", "at"], "a": "through"},
        {"q": "The picture hangs _____ the fireplace.", "options": ["above", "over", "on", "up"], "a": "above"},
        {"q": "The dog sat _____ its master.", "options": ["beside", "besides", "between", "among"], "a": "beside"},
        {"q": "We climbed _____ the hill to see the view.", "options": ["up", "onto", "over", "above"], "a": "up"},
        {"q": "The ring slipped _____ her finger.", "options": ["off", "of", "from", "away"], "a": "off"},
        {"q": "The lizard disappeared _____ the rocks.", "options": ["among", "between", "into", "under"], "a": "among"},
        {"q": "He jumped _____ the puddle to stay dry.", "options": ["over", "across", "through", "above"], "a": "over"},
        {"q": "The train passed _____ the station without stopping.", "options": ["through", "past", "along", "across"], "a": "through"},
        {"q": "The fruit fell _____ the basket.", "options": ["out of", "from", "off", "away"], "a": "out of"},
        {"q": "The submarine traveled _____ the ocean surface.", "options": ["below", "under", "beneath", "down"], "a": "below"},
        {"q": "He stood _____ the front of the queue.", "options": ["at", "in", "on", "by"], "a": "at"},
        {"q": "The helicopter hovered _____ the building.", "options": ["over", "above", "across", "up"], "a": "over"},
        {"q": "The athlete ran _____ the track ten times.", "options": ["around", "across", "along", "through"], "a": "around"},
        {"q": "She put the letter _____ the envelope.", "options": ["inside", "into", "within", "in"], "a": "inside"},
        {"q": "The path leads _____ the dark forest.", "options": ["through", "along", "across", "over"], "a": "through"},
        {"q": "He threw the ball _____ the fence.", "options": ["over", "above", "across", "past"], "a": "over"},
        {"q": "The shop is located _____ the street from the bank.", "options": ["across", "opposite", "along", "beside"], "a": "across"},
        {"q": "We traveled _____ bus to the zoo.", "options": ["by", "with", "in", "on"], "a": "by"},
        {"q": "He arrived _____ school early.", "options": ["at", "in", "to", "on"], "a": "at"},
        {"q": "The stars shine _____ the sky.", "options": ["in", "at", "on", "above"], "a": "in"},
        {"q": "She hung her coat _____ the hook.", "options": ["on", "at", "to", "onto"], "a": "on"},
        {"q": "The boat sailed _____ the bridge.", "options": ["under", "below", "beneath", "across"], "a": "under"},
        {"q": "He sat _____ his two best friends.", "options": ["between", "among", "beside", "next"], "a": "between"},
        {"q": "They walked _____ the museum together.", "options": ["through", "across", "along", "around"], "a": "through"},
        {"q": "The cat is sleeping _____ the rug.", "options": ["on", "at", "in", "onto"], "a": "on"}
      ],
      "Editing (Typing)": [
        {"q": "Fix the misspelled word: 'She wore beautiful JEWELRY.'", "a": "jewellery"},
        {"q": "Fix the misspelled word: 'The LION was very FEROSIOUS.'", "a": "ferocious"},
        {"q": "Fix the misspelled word: 'We stood in a long QUENE.'", "a": "queue"},
        {"q": "Fix the misspelled word: 'He is an INVINCIBLE opponent.'", "a": "invincible"},
        {"q": "Fix the misspelled word: 'I will see you TOMMORO.'", "a": "tomorrow"},
        {"q": "Fix the misspelled word: 'Check the CALENDER for the date.'", "a": "calendar"},
        {"q": "Fix the misspelled word: 'The NAYBOR was very kind.'", "a": "neighbour"},
        {"q": "Fix the misspelled word: 'Keep the two items SEPERATE.'", "a": "separate"},
        {"q": "Fix the misspelled word: 'I don't BELEIVE you.'", "a": "believe"},
        {"q": "Fix the misspelled word: 'It happened IMEDIATLY.'", "a": "immediately"},
        {"q": "Fix the misspelled word: 'The soldier wore CAMOFLAGE.'", "a": "camouflage"},
        {"q": "Fix the misspelled word: 'She felt MISERABEL today.'", "a": "miserable"},
        {"q": "Fix the misspelled word: 'It was the BEGINING of the race.'", "a": "beginning"},
        {"q": "Fix the misspelled word: 'The box was very HEAVY.'", "a": "heavy"},
        {"q": "Fix the misspelled word: 'I have ENOUGH food.'", "a": "enough"},
        {"q": "Fix the misspelled word: 'He is my worst OPPONANT.'", "a": "opponent"},
        {"q": "Fix the misspelled word: 'Remember to BREATHE deeply.'", "a": "breathe"},
        {"q": "Fix the misspelled word: 'The CHAMPONSIP was exciting.'", "a": "championship"},
        {"q": "Fix the misspelled word: 'He had great STRENTH.'", "a": "strength"},
        {"q": "Fix the misspelled word: 'The view was BEATIFUL.'", "a": "beautiful"},
        {"q": "Fix the misspelled word: 'That is a STRANGE UNIFROM.'", "a": "uniform"},
        {"q": "Fix the misspelled word: 'My STOMACK hurts.'", "a": "stomach"},
        {"q": "Fix the misspelled word: 'I FINALY finished my work.'", "a": "finally"},
        {"q": "Fix the misspelled word: 'The FOTOGRAPH was blurry.'", "a": "photograph"},
        {"q": "Fix the misspelled word: 'He is a famous PAINTER.'", "a": "painter"},
        {"q": "Fix the misspelled word: 'I am SEARCHING for my keys.'", "a": "searching"},
        {"q": "Fix the misspelled word: 'The GALLERY was quiet.'", "a": "gallery"},
        {"q": "Fix the misspelled word: 'She is a very SPECIAL person.'", "a": "special"},
        {"q": "Fix the misspelled word: 'The weather is PLEASANT.'", "a": "pleasant"},
        {"q": "Fix the misspelled word: 'I need to PRACTICE my piano.'", "a": "practice"},
        {"q": "Fix the misspelled word: 'The library was SILENT.'", "a": "silent"},
        {"q": "Fix the misspelled word: 'He is a COURAGEOUS boy.'", "a": "courageous"},
        {"q": "Fix the misspelled word: 'The juice was DELICIOUS.'", "a": "delicious"},
        {"q": "Fix the misspelled word: 'I was SUPRISED by the news.'", "a": "surprised"},
        {"q": "Fix the misspelled word: 'He has a lot of KNOWLEDGE.'", "a": "knowledge"},
        {"q": "Fix the misspelled word: 'It is a PRIVILEGE to be here.'", "a": "privilege"},
        {"q": "Fix the misspelled word: 'The teacher gave a MESSAG.'", "a": "message"},
        {"q": "Fix the misspelled word: 'I received a PRESANT.'", "a": "present"},
        {"q": "Fix the misspelled word: 'The animal was DANGEROUS.'", "a": "dangerous"},
        {"q": "Fix the misspelled word: 'I have a big DILEMMA.'", "a": "dilemma"},
        {"q": "Fix the misspelled word: 'She is very INTELLIGENT.'", "a": "intelligent"},
        {"q": "Fix the misspelled word: 'The PARTY was fun.'", "a": "party"},
        {"q": "Fix the misspelled word: 'He is an HONEST man.'", "a": "honest"},
        {"q": "Fix the misspelled word: 'The ocean is ENORMOUS.'", "a": "enormous"},
        {"q": "Fix the misspelled word: 'I need some ADVISE.'", "a": "advice"},
        {"q": "Fix the misspelled word: 'The cat was CHASSING the mouse.'", "a": "chasing"},
        {"q": "Fix the misspelled word: 'He is very GRATEFULL.'", "a": "grateful"},
        {"q": "Fix the misspelled word: 'The story was EXCITING.'", "a": "exciting"},
        {"q": "Fix the misspelled word: 'I am VERY happy.'", "a": "very"},
        {"q": "Fix the misspelled word: 'The sky is BRIGHT.'", "a": "bright"}
      ],
      "Grammar Cloze": [
        {"q": "The old art _____ was quiet and dusty.", "options": ["gallery", "museum", "studio", "hall"], "a": "gallery"},
        {"q": "As Jude stepped _____ the room, he saw paintings.", "options": ["into", "onto", "to", "at"], "a": "into"},
        {"q": "_____ the room was dark, he saw a photograph.", "options": ["Although", "Because", "Since", "Despite"], "a": "Although"},
        {"q": "Suddenly, his _____ rumbled with hunger.", "options": ["stomach", "stomack", "stomac", "stumack"], "a": "stomach"},
        {"q": "He _____ decided to head home.", "options": ["finally", "finaly", "final", "finnaly"], "a": "finally"},
        {"q": "The teacher _____ the students to be quiet.", "options": ["told", "said", "asked", "ordered"], "a": "told"},
        {"q": "The bird flew _____ the sky.", "options": ["across", "through", "in", "along"], "a": "across"},
        {"q": "She _____ her homework before dinner.", "options": ["finished", "finishes", "finish", "finishing"], "a": "finished"},
        {"q": "The cat sat _____ the warm rug.", "options": ["on", "at", "in", "to"], "a": "on"},
        {"q": "He was _____ when he saw the surprise.", "options": ["happy", "sad", "angry", "surprised"], "a": "surprised"},
        {"q": "The sun _____ brightly today.", "options": ["shines", "shone", "shine", "shining"], "a": "shines"},
        {"q": "They _____ to the park every Sunday.", "options": ["go", "goes", "going", "went"], "a": "go"},
        {"q": "The water in the lake was _____.", "options": ["cold", "hot", "warm", "cool"], "a": "cold"},
        {"q": "She _____ a beautiful song.", "options": ["sang", "sing", "sings", "singing"], "a": "sang"},
        {"q": "The leaves fell _____ the trees in autumn.", "options": ["from", "off", "out of", "away"], "a": "from"},
        {"q": "He is the _____ boy in the class.", "options": ["tallest", "taller", "tall", "talls"], "a": "tallest"},
        {"q": "I _____ my teeth every morning.", "options": ["brush", "brushes", "brushed", "brushing"], "a": "brush"},
        {"q": "The dog _____ at the stranger.", "options": ["barked", "bark", "barks", "barking"], "a": "barked"},
        {"q": "She put the books _____ the shelf.", "options": ["on", "at", "in", "to"], "a": "on"},
        {"q": "The rain _____ heavily last night.", "options": ["fell", "fall", "falls", "falling"], "a": "fell"},
        {"q": "He _____ a lot of books in the library.", "options": ["reads", "read", "reading", "readed"], "a": "reads"},
        {"q": "The flowers _____ in the garden.", "options": ["grow", "grows", "growing", "grew"], "a": "grow"},
        {"q": "She _____ a letter to her grandmother.", "options": ["wrote", "write", "writes", "writing"], "a": "wrote"},
        {"q": "The cake _____ delicious.", "options": ["was", "is", "were", "are"], "a": "was"},
        {"q": "They _____ football in the afternoon.", "options": ["play", "plays", "playing", "played"], "a": "play"},
        {"q": "The mountain was very _____.", "options": ["high", "tall", "big", "large"], "a": "high"},
        {"q": "He _____ a red car.", "options": ["drives", "drive", "driving", "drove"], "a": "drives"},
        {"q": "She _____ her umbrella because it was raining.", "options": ["took", "takes", "take", "taking"], "a": "took"},
        {"q": "The stars _____ at night.", "options": ["twinkle", "twinkles", "twinkling", "twinkled"], "a": "twinkle"},
        {"q": "He is _____ than his brother.", "options": ["older", "oldest", "old", "olds"], "a": "older"},
        {"q": "The baby _____ for milk.", "options": ["cried", "cry", "cries", "crying"], "a": "cried"},
        {"q": "They _____ to the cinema last night.", "options": ["went", "go", "goes", "going"], "a": "went"},
        {"q": "The apple was _____ and sweet.", "options": ["red", "green", "yellow", "blue"], "a": "red"},
        {"q": "She _____ a new dress for the party.", "options": ["bought", "buy", "buys", "buying"], "a": "bought"},
        {"q": "The wind _____ strongly during the storm.", "options": ["blew", "blow", "blows", "blowing"], "a": "blew"},
        {"q": "He _____ the door quietly.", "options": ["closed", "close", "closes", "closing"], "a": "closed"},
        {"q": "The children _____ loudly in the playground.", "options": ["shouted", "shout", "shouts", "shouting"], "a": "shouted"},
        {"q": "She _____ her breakfast early.", "options": ["ate", "eat", "eats", "eating"], "a": "ate"},
        {"q": "The box was _____ to carry.", "options": ["heavy", "light", "big", "small"], "a": "heavy"},
        {"q": "He _____ his keys on the table.", "options": ["left", "leave", "leaves", "leaving"], "a": "left"},
        {"q": "They _____ a lot of fun at the beach.", "options": ["had", "have", "has", "having"], "a": "had"},
        {"q": "The river is _____ and deep.", "options": ["wide", "narrow", "long", "short"], "a": "wide"},
        {"q": "She _____ a picture of a house.", "options": ["drew", "draw", "draws", "drawing"], "a": "drew"},
        {"q": "The clock _____ loudly.", "options": ["ticked", "tick", "ticks", "ticking"], "a": "ticked"},
        {"q": "He _____ his father in the garden.", "options": ["helped", "help", "helps", "helping"], "a": "helped"},
        {"q": "The moon _____ brightly in the sky.", "options": ["shone", "shine", "shines", "shining"], "a": "shone"},
        {"q": "They _____ a nest in the tree.", "options": ["found", "find", "finds", "finding"], "a": "found"},
        {"q": "She _____ to the radio every morning.", "options": ["listens", "listen", "listening", "listened"], "a": "listens"},
        {"q": "The car _____ slowly down the street.", "options": ["moved", "move", "moves", "moving"], "a": "moved"},
        {"q": "He _____ his best in the exam.", "options": ["did", "do", "does", "doing"], "a": "did"}
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
