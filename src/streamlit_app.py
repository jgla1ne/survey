import streamlit as st

# Define the quiz questions and options
quiz = [
    {
        "question": "1. Vision for Our Future\nHow do you see our relationship evolving?",
        "options": {
            "A": "I believe rebuilding trust can lead to a renewed, intimate future together.",
            "B": "I feel too hurt, and certain behaviors have created a barrier I may not overcome.",
            "C": "I envision us remaining supportive friends and committed co-parents without a romantic element."
        }
    },
    {
        "question": "2. Trust and Vulnerability\nHow comfortable do you feel opening up and being vulnerable with me?",
        "options": {
            "A": "I feel safe enough to share my innermost thoughts, hopeful for a deeper bond.",
            "B": "I'm guarded because past hurts make it difficult to trust you again.",
            "C": "I can talk to you when needed, though I see our connection primarily as cooperative rather than intimate."
        }
    },
    {
        "question": "3. Emotional Impact of Past Conflicts\nWhen thinking about past conflicts, what best describes your feelings?",
        "options": {
            "A": "I see them as challenges we can work through together to build a stronger foundation.",
            "B": "They’re reminders of behavior I still struggle to move past, affecting my trust.",
            "C": "I view them as important lessons that define our adult, practical relationship."
        }
    },
    {
        "question": "4. Readiness to Work on the Relationship\nConsidering our separation, how open are you to efforts (such as counseling) to heal emotionally and rebuild trust?",
        "options": {
            "A": "I'm very open to working together for a future together.",
            "B": "I'm not sure I can heal from the past; my feelings are too painful right now.",
            "C": "I'm willing to engage in practical steps that help us collaborate better as co-parents and friends."
        }
    },
    {
        "question": "5. Perception of Personal Change\nHow do you see the possibility of personal change influencing our relationship?",
        "options": {
            "A": "I believe that changes—in behavior, mindset, or circumstances—could pave the way for a renewed bond.",
            "B": "I'm skeptical that significant change will occur given the patterns of behavior I've observed.",
            "C": "I see the potential for respectful personal improvement that supports our partnership as friends and parents."
        }
    },
    {
        "question": "6. Communication Quality\nHow would you rate the quality of our communication now?",
        "options": {
            "A": "I feel our communication has the potential to improve into a deeper, more supportive dialogue.",
            "B": "Our communication still feels strained and painful, reinforcing my distrust.",
            "C": "I consider our exchanges functional, which is enough for cooperation as partners in parenting."
        }
    },
    {
        "question": "7. Emotional Safety\nDo you feel emotionally safe around me?",
        "options": {
            "A": "Yes—I feel that we can create a space of mutual respect and understanding that might lead to an intimate partnership.",
            "B": "No—I still experience emotional risks that make it hard to feel safe.",
            "C": "I feel safe enough for constructive dialogue, but I perceive our relationship as a stable, non-romantic partnership."
        }
    },
    {
        "question": "8. Co-Parenting Dynamics\nHow do you feel about our ability to collaborate effectively for the well-being of our children?",
        "options": {
            "A": "I believe that healing our emotional connection will also enrich our co-parenting.",
            "B": "The unresolved issues hinder my ability to fully trust you as a partner in parenting.",
            "C": "I'm confident that we can maintain a respectful, cooperative relationship strictly for our children’s benefit."
        }
    },
    {
        "question": "9. Desire for Intimacy\nHow would you describe your current desire for emotional or physical intimacy with me?",
        "options": {
            "A": "I still have a strong desire to connect on an intimate, romantic level.",
            "B": "I find it challenging to see beyond the past behaviors that have hurt me.",
            "C": "I prefer keeping our interactions supportive and focused on friendship/parenting roles."
        }
    },
    {
        "question": "10. Overall Relationship Outlook\nTaking everything into account, how would you summarize your feelings about our relationship's potential?",
        "options": {
            "A": "I'm hopeful we can work through our challenges and re-establish a strong, loving bond.",
            "B": "I'm deeply conflicted and uncertain if our issues can be overcome.",
            "C": "I value our current dynamic as friends and co-parents, without the desire to rekindle a romantic connection."
        }
    }
]

st.title("Relationship Reflection Quiz")

st.write("For each question, select the option that best describes your feelings.")

# Dictionary to store the user's answers
answers = {}

with st.form(key="quiz_form"):
    for idx, q in enumerate(quiz):
        option = st.radio(q["question"], list(q["options"].keys()), key=f"q{idx}")
        answers[f"q{idx}"] = option
    submitted = st.form_submit_button(label="Submit")

if submitted:
    st.subheader("Your Responses")
    for idx, q in enumerate(quiz):
        answer = answers[f"q{idx}"]
        st.write(f"Q{idx+1}: Option {answer} - {q['options'][answer]}")
    
    # Simple scoring logic by counting answers. Customize as needed.
    score_counts = {"A": 0, "B": 0, "C": 0}
    for answer in answers.values():
        score_counts[answer] += 1

    st.subheader("Quiz Summary")
    st.write("Option counts:")
    st.write(score_counts)
    
    # Determine a simple result based on majority answer
    majority = max(score_counts, key=score_counts.get)
    if majority == "A":
        result = "Your responses indicate hope for a renewed, intimate partnership."
    elif majority == "B":
        result = "Your responses suggest ongoing hurt and challenges in trusting."
    else:
        result = "Your responses prioritize current relationships as friends and co-parents."

    st.write("Result:", result)