import streamlit as st
from typing import List
from services.interview.voice_coach import generate_interview_questions, evaluate_spoken_answer


def render_mock_interview_page(skills: List[str]) -> None:
    """
    Renders Real HR AI Interviewer & Voice Communication Coach Interface.
    """
    st.title("🎙️ AI HR Interviewer & Voice Communication Coach")
    st.write(
        "Practice realistic interview questions tailored to your resume. "
        "Get instant feedback on your **Technical Knowledge** and **English Communication Skills**."
    )

    if not skills:
        st.warning("Please upload your resume first to generate personalized HR interview questions.")
        return

    st.markdown("---")

    questions = generate_interview_questions(skills)

    # Question Selection
    st.subheader("1. HR Interview Question")
    question_options = [f"[{q['skill']}] {q['question']}" for q in questions]
    selected_idx = st.selectbox(
        "Select Question to Practice:",
        range(len(question_options)),
        format_func=lambda i: question_options[i]
    )

    selected_q = questions[selected_idx]

    # HR Card
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 22px; border-radius: 10px; color: #ffffff; margin: 16px 0;">
            <p style="color: #94a3b8; font-size: 12px; font-weight: 600; text-transform: uppercase; margin: 0;">Virtual HR Interviewer Asks:</p>
            <h3 style="color: #ffffff; margin-top: 8px; font-size: 19px; font-weight: 600;">"{selected_q['question']}"</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Answer Input Section
    st.subheader("2. Your Answer (Record Voice or Type Transcript)")

    audio_val = st.audio_input("Record your answer (Voice):")
    manual_text = st.text_area(
        "Or type/paste your spoken answer text:",
        height=130,
        placeholder="Example: In Python, memory management is handled by the Python Memory Manager via private heaps and reference counting..."
    )

    answer_text = ""
    if audio_val:
        st.audio(audio_val)
        answer_text = manual_text if manual_text else "Recorded audio answer submitted for HR evaluation."
    elif manual_text:
        answer_text = manual_text

    if st.button("Submit Answer to HR Evaluator", type="primary"):
        if not answer_text:
            st.error("Please record audio or enter text before submitting.")
            return

        feedback = evaluate_spoken_answer(selected_q['question'], answer_text)

        st.markdown("---")
        st.subheader("📊 HR Evaluation & Diagnostic Metrics")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Technical Depth", f"{feedback['tech_score']}%")
        with col2:
            st.metric("Clarity & Fluency", f"{feedback['clarity_score']}%")
        with col3:
            st.metric("Confidence Rating", f"{feedback['confidence_score']}%")

        # Communication Tips
        st.markdown("### 💬 Communication & Grammar Analysis")
        st.info(feedback["communication_tips"])

        if feedback["filler_words_detected"]:
            st.warning(f"⚠️ **Filler Words Detected:** {', '.join(feedback['filler_words_detected'])}")

        # HR Advice Card
        st.markdown("### 👔 HR Recommendation")
        st.success(feedback["hr_feedback"])