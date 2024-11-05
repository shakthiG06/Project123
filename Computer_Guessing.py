import streamlit as st

st.set_page_config(page_title="GS Game House")
if 'low' not in st.session_state:
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.attempts = 7
    st.session_state.guess = None
    st.session_state.game_over = False

st.title("Computer Guessing Game")
st.write("Think of a number between 1 and 100. The computer will try to guess it in 7 tries!")

if not st.session_state.game_over:
    
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
    st.write(f"Computer's guess: {st.session_state.guess}")

    
    feedback = st.radio("Is the guess correct?", ["Correct", "Too Low", "Too High"], key="feedback")

    if st.button("Submit"):
        if feedback == "Correct":
            st.success(f"Yay! The computer guessed your number {st.session_state.guess} correctly!")
            st.balloons()
            st.session_state.game_over = True
        elif feedback == "Too Low":
            st.session_state.low = st.session_state.guess + 1
            st.session_state.attempts -= 1
        elif feedback == "Too High":
            st.session_state.high = st.session_state.guess - 1
            st.session_state.attempts -= 1

        
        if st.session_state.attempts <= 0:
            st.error("Game over! The computer couldn't guess your number.")
            st.session_state.game_over = True

    
    st.write(f"Attempts left: {st.session_state.attempts}")


if st.button("Restart Game"):
    st.session_state.clear()