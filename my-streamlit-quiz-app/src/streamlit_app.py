import streamlit as st

def load_quiz():
    with open("quizz.md", "r") as file:
        return file.read()

def render_quiz(quiz_content):
    st.markdown(quiz_content)

def main():
    st.title("Relationship Quiz")
    quiz_content = load_quiz()
    render_quiz(quiz_content)

if __name__ == "__main__":
    main()