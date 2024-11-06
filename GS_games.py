import streamlit as st


st.set_page_config(page_title="GS Game House")
st.header("GS Guessing")
st.write("In your guessing game, the goal is for players to identify a number within seven tries.Players will receive clues or hints related to the target word, and they must use their deduction skills to make educated guesses.The challenge lies in the limited number of attempts, encouraging strategic thinking and careful consideration of each guess.The game promotes fun and excitement as players work to uncover the mystery before running out of tries!")


st.header("How to Play a Number Guessing Game?")
st.title("1. Setup:")
st.text("Choose a range for the number (e.g., between 1 and 100).")
st.text("Select a secret number within that range and keep it hidden from the players.")

st.title("2. Objective:")
st.text("Players must guess the secret number within 7 attempts.")

st.title("3. Game Play:")
st.write("Players take turns guessing a number within the defined range.")
st.write("After each guess, you provide feedback:")
st.write("“Too high” if the guess is above the secret number.")
st.write("“Too low” if the guess is below the secret number.")
st.write("“Correct!” if the guess matches the secret number.")

st.title("4 .Limit Attempts:")
st.write("Players have a maximum of 7 tries to guess the correct number. Keep track of the number of attempts.")

st.title("5. Winning:")
st.write("If a player guesses the number within 7 tries, they win!")
st.write("If all attempts are used without a correct guess, reveal the secret number.")

st.title("6. Repeat:")
st.write("After a round, players can choose a new secret number and continue playing, or switch roles so different players can hide a number.")
