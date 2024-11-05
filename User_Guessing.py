import streamlit as st
import random


st.set_page_config(page_title="GS Game House")
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 7
    st.session_state.guesses = []


st.title("Guess the Number Game")
st.write("I'm thinking of a number between 1 and 100. You have 7 tries to guess it!")


guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    if guess in st.session_state.guesses:
        st.warning("You've already guessed that number! Try a different one.")
    else:
        st.session_state.guesses.append(guess)
        st.session_state.attempts -= 1

        if guess == st.session_state.secret_number:
            st.success(f"Congratulations! You guessed the number {st.session_state.secret_number}!")
            st.balloons()
            st.session_state.clear()  
        elif st.session_state.attempts <= 0:
            st.error(f"Out of attempts! The number was {st.session_state.secret_number}.")
            st.session_state.clear()  
        elif guess < st.session_state.secret_number:
            st.info("Too low! Try again.")
        else:
            st.info("Too high! Try again.")


st.write(f"You have {st.session_state.attempts} attempts left.")


if st.button("Restart Game"):
    st.session_state.clear()  