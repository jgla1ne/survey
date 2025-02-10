# FILE: /streamlit-quiz-app/streamlit-quiz-app/app.py
import streamlit as st
from utils.quiz import load_questions, calculate_score

def main():
    st.title("Relationship Quiz")
    
    questions = load_questions()
    responses = []
    
    for question in questions:
        st.subheader(question['question'])
        response = st.radio("Select your response:", question['options'])
        responses.append(response)

    if st.button("Submit"):
        score = calculate_score(responses)
        st.write(f"Your score is: {score}/{len(questions)}")
        st.balloons()

if __name__ == "__main__":
    main()