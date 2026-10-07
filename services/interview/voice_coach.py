import re
from typing import Dict, Any, List

# Multi-Domain HR Question Bank based on Skills
DOMAIN_HR_QUESTIONS = {
    # Software & AI Skills
    "python": [
        "I see Python listed on your resume. How do you handle memory management and garbage collection in Python?",
        "Tell me about a complex bug you faced in a Python project and how you debugged it."
    ],
    "machine learning": [
        "Can you walk me through a machine learning model you built from scratch? How did you evaluate its accuracy?",
        "How do you handle overfitting and underfitting when training your models?"
    ],
    "sql": [
        "What is the difference between WHERE and HAVING clauses in SQL, and when would you optimize a query using indexes?",
        "Describe a scenario where you had to write a complex JOIN query for data extraction."
    ],
    "rag": [
        "You mentioned RAG on your resume. How do you select chunk size and vector embedding models for optimal retrieval?"
    ],
    "power bi": [
        "How do you decide between calculated columns and DAX measures when designing a Power BI dashboard?"
    ],

    # EEE & ECE Skills
    "embedded systems": [
        "Can you explain the difference between a microcontroller and a microprocessor based on a project you worked on?",
        "How do you handle real-time interrupt handling in embedded systems?"
    ],
    "matlab": [
        "How have you utilized MATLAB for system simulation or signal processing in your academic/core projects?"
    ],
    "plc": [
        "Explain how you design logic for a PLC system and how you troubleshoot hardware communication faults."
    ],

    # Healthcare Skills
    "patient care": [
        "How do you prioritize patient care when managing multiple high-acuity patients during a busy shift?",
        "Describe a situation where a patient or family member was upset. How did you handle communication empathetically?"
    ],
    "cpr": [
        "Walk me through the standard BLS/CPR protocol in a clinical emergency situation."
    ],

    # Mechanical & Civil Skills
    "autocad": [
        "How do you ensure precision and standard layer management when creating 2D/3D models in AutoCAD?",
        "Describe a mechanical/structural design project you completed and the engineering constraints you faced."
    ],

    # Universal Soft Skills
    "communication": [
        "Tell me about yourself, your top technical projects, and why you are a strong fit for this role."
    ],
    "teamwork": [
        "Tell me about a time you had a difference of opinion with a team member on a project. How did you reach a consensus?"
    ]
}


def generate_interview_questions(skills: List[str]) -> List[Dict[str, str]]:
    """
    Generates realistic HR questions tailored directly to candidate resume skills.
    """
    questions = []
    user_skills_lower = [s.lower() for s in skills]

    for skill_name, q_list in DOMAIN_HR_QUESTIONS.items():
        if skill_name in user_skills_lower:
            for q in q_list:
                questions.append({
                    "skill": skill_name.title(),
                    "question": q
                })

    if not questions:
        questions.extend([
            {
                "skill": "HR Profile",
                "question": "Tell me about yourself, your background, and your key academic or professional achievements."
            },
            {
                "skill": "HR Behavioral",
                "question": "What is your biggest technical or professional challenge so far, and how did you overcome it?"
            }
        ])

    return questions[:6]


def evaluate_spoken_answer(question: str, spoken_text: str) -> Dict[str, Any]:
    """
    Evaluates candidate spoken or typed response like a real HR Manager.
    Returns clear, professional English feedback for communication and technical depth.
    """
    if not spoken_text or len(spoken_text.strip()) < 15:
        return {
            "clarity_score": 25,
            "tech_score": 20,
            "confidence_score": 30,
            "filler_words_detected": [],
            "communication_tips": "Your response is too brief. To improve speech clarity and structure, aim to speak for 30–45 seconds using the STAR method (Situation, Task, Action, Result).",
            "hr_feedback": "HR View: An incomplete or overly brief answer creates an impression of insufficient preparation or lack of technical depth."
        }

    text_lower = spoken_text.lower()
    words = text_lower.split()
    word_count = len(words)

    # Detect Filler Words
    fillers = ["um", "uh", "like", "basically", "you know", "actually"]
    detected_fillers = [w for w in words if w in fillers]
    filler_count = len(detected_fillers)

    clarity_score = max(35, min(95, 100 - (filler_count * 5) + min(25, word_count // 3)))
    tech_score = max(40, min(98, 45 + (min(40, word_count // 2))))
    confidence_score = max(35, min(95, clarity_score - (filler_count * 3)))

    feedback_points = []
    if filler_count > 2:
        feedback_points.append(
            f"Frequent filler words detected ({', '.join(set(detected_fillers))}). "
            "Try substituting silent pauses instead of filler words to maintain professional flow."
        )
    else:
        feedback_points.append("Excellent verbal flow with minimal filler word usage.")

    if word_count < 35:
        feedback_points.append("Consider providing a more detailed answer by including a concrete project example.")
    else:
        feedback_points.append("Good answer depth and well-structured coverage.")

    return {
        "clarity_score": clarity_score,
        "tech_score": tech_score,
        "confidence_score": confidence_score,
        "filler_words_detected": list(set(detected_fillers)),
        "communication_tips": " ".join(feedback_points),
        "hr_feedback": f"HR Recommendation: For '{question}', begin with a clear technical definition, link it to practical project experience from your resume, and conclude with the outcome or impact."
    }