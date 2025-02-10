def load_questions():
    questions = [
        {
            "question": "How do you see our relationship evolving?",
            "options": {
                "A": "I believe rebuilding trust can lead to a renewed, intimate future together.",
                "B": "I feel too hurt, and certain behaviors have created a barrier I may not overcome.",
                "C": "I envision us remaining supportive friends and committed co-parents without a romantic element."
            }
        },
        {
            "question": "How comfortable do you feel opening up and being vulnerable with me?",
            "options": {
                "A": "I feel safe enough to share my innermost thoughts, hopeful for a deeper bond.",
                "B": "I’m guarded because past hurts make it difficult to trust you again.",
                "C": "I can talk to you when needed, though I see our connection primarily as cooperative rather than intimate."
            }
        },
        {
            "question": "When thinking about past conflicts, what best describes your feelings?",
            "options": {
                "A": "I see them as challenges we can work through together to build a stronger foundation.",
                "B": "They’re reminders of behavior I still struggle to move past, affecting my trust.",
                "C": "I view them as important lessons that define our adult, practical relationship."
            }
        },
        {
            "question": "Considering our separation, how open are you to efforts (such as counseling) to heal emotionally and rebuild trust?",
            "options": {
                "A": "I’m very open to working together for a future together.",
                "B": "I’m not sure I can heal from the past; my feelings are too painful right now.",
                "C": "I’m willing to engage in practical steps that help us collaborate better as co-parents and friends."
            }
        },
        {
            "question": "How do you see the possibility of personal change (in either of us) influencing our relationship?",
            "options": {
                "A": "I believe that changes—in behavior, mindset, or circumstances—could pave the way for a renewed bond.",
                "B": "I’m skeptical that significant change will occur given the patterns of behavior I’ve observed.",
                "C": "I see the potential for respectful personal improvement that supports our partnership as friends and parents."
            }
        },
        {
            "question": "How would you rate the quality of our communication now?",
            "options": {
                "A": "I feel our communication has the potential to improve into a deeper, more supportive dialogue.",
                "B": "Our communication still feels strained and painful, reinforcing my distrust.",
                "C": "I consider our exchanges functional, which is enough for cooperation as partners in parenting."
            }
        },
        {
            "question": "Do you feel emotionally safe around me?",
            "options": {
                "A": "Yes—I feel that we can create a space of mutual respect and understanding that might lead to an intimate partnership.",
                "B": "No—I still experience emotional risks that make it hard to feel safe.",
                "C": "I feel safe enough for constructive dialogue, but I perceive our relationship as a stable, non-romantic partnership."
            }
        },
        {
            "question": "How do you feel about our ability to collaborate effectively for the well-being of our children?",
            "options": {
                "A": "I believe that healing our emotional connection will also enrich our co-parenting.",
                "B": "The unresolved issues hinder my ability to fully trust you as a partner in parenting.",
                "C": "I’m confident that we can maintain a respectful, cooperative relationship strictly for our children’s benefit."
            }
        },
        {
            "question": "How would you describe your current desire for emotional or physical intimacy with me?",
            "options": {
                "A": "I still have a strong desire to connect on an intimate, romantic level.",
                "B": "I find it challenging to see beyond the past behaviors that have hurt me.",
                "C": "I prefer keeping our interactions supportive and focused on friendship/parenting roles."
            }
        },
        {
            "question": "Taking everything into account, how would you summarize your feelings about our relationship’s potential?",
            "options": {
                "A": "I’m hopeful we can work through our challenges and re-establish a strong, loving bond.",
                "B": "I’m deeply conflicted and uncertain if our issues can be overcome.",
                "C": "I value our current dynamic as friends and co-parents, without the desire to rekindle a romantic connection."
            }
        }
    ]
    return questions

def calculate_score(responses):
    score = 0
    for response in responses:
        if response == 'A':
            score += 2
        elif response == 'B':
            score += 1
        elif response == 'C':
            score += 0
    return score

def get_result(score):
    if score >= 15:
        return "High potential for a positive relationship."
    elif score >= 10:
        return "Moderate potential for improvement."
    else:
        return "Low potential for a positive relationship."