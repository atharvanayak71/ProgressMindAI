import streamlit as st
import requests

API_URL = "http://127.0.0.1:8080"

st.set_page_config(
    page_title="ProgressMind",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        background-color: #0a0a0f;
        color: #e2e8f0;
    }

    .stApp { background: #0a0a0f; }

    [data-testid="stSidebar"] {
        background: #0d0d1a !important;
        border-right: 1px solid #1a1a2e !important;
    }

    .sidebar-brand {
        font-family: 'Space Mono', monospace;
        font-size: 1.3rem;
        font-weight: 700;
        color: #8b5cf6;
        text-align: center;
        padding: 2rem 0 0.3rem 0;
        letter-spacing: -0.5px;
    }

    .sidebar-sub {
        font-size: 0.7rem;
        color: #334155;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 1.5rem;
    }

    .hero {
        background: linear-gradient(135deg, #120820 0%, #0d0d1a 45%, #07101f 100%);
        border: 1px solid #1a1a2e;
        border-radius: 14px;
        padding: 2.5rem 2.5rem 2rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }

    .hero::after {
        content: '';
        position: absolute;
        top: 0; right: 0;
        width: 40%;
        height: 100%;
        background: radial-gradient(ellipse at right, rgba(139, 92, 246, 0.07) 0%, transparent 70%);
        pointer-events: none;
    }

    .hero-tag {
        display: inline-block;
        font-family: 'Space Mono', monospace;
        font-size: 0.65rem;
        color: #8b5cf6;
        border: 1px solid rgba(139, 92, 246, 0.35);
        background: rgba(139, 92, 246, 0.08);
        padding: 0.2rem 0.8rem;
        border-radius: 100px;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 1rem;
    }

    .hero-title {
        font-family: 'Space Mono', monospace;
        font-size: 2.1rem;
        font-weight: 700;
        color: #f8fafc;
        letter-spacing: -1.5px;
        line-height: 1.1;
        margin-bottom: 0.6rem;
    }

    .hero-title em {
        font-style: normal;
        color: #8b5cf6;
    }

    .hero-desc {
        font-size: 0.9rem;
        color: #475569;
        font-weight: 300;
        letter-spacing: 0.01em;
        line-height: 1.6;
    }

    .section-label {
        font-family: 'Space Mono', monospace;
        font-size: 0.65rem;
        font-weight: 700;
        color: #334155;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        margin-bottom: 0.4rem;
    }

    .stTextArea textarea {
        background: #0d0d1a !important;
        border: 1px solid #1a1a2e !important;
        border-radius: 8px !important;
        color: #cbd5e1 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.88rem !important;
        line-height: 1.6 !important;
        resize: vertical !important;
        transition: border-color 0.15s !important;
    }

    .stTextArea textarea:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1) !important;
        outline: none !important;
    }

    .stTextArea textarea::placeholder {
        color: #2d3748 !important;
        font-style: italic !important;
    }

    .stTextInput input {
        background: #0d0d1a !important;
        border: 1px solid #1a1a2e !important;
        border-radius: 8px !important;
        color: #cbd5e1 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.88rem !important;
    }

    .stTextInput input:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1) !important;
    }

    .stTextInput input::placeholder {
        color: #2d3748 !important;
        font-style: italic !important;
    }

    .stTextArea label, .stTextInput label {
        font-family: 'Space Mono', monospace !important;
        font-size: 0.65rem !important;
        font-weight: 700 !important;
        color: #475569 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.12em !important;
    }

    .stButton > button {
        background: #8b5cf6 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.7rem 2rem !important;
        font-family: 'Space Mono', monospace !important;
        font-weight: 700 !important;
        font-size: 0.75rem !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
        width: 100% !important;
        transition: all 0.15s ease !important;
    }

    .stButton > button:hover {
        background: #7c3aed !important;
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.3) !important;
        transform: translateY(-1px) !important;
    }

    .stButton > button:active {
        transform: translateY(0px) !important;
        box-shadow: none !important;
    }

    .result-wrap {
        margin-top: 2rem;
        border: 1px solid #1a1a2e;
        border-left: 3px solid #8b5cf6;
        border-radius: 10px;
        overflow: hidden;
    }

    .result-header {
        background: #0d0d1a;
        padding: 0.75rem 1.5rem;
        font-family: 'Space Mono', monospace;
        font-size: 0.65rem;
        color: #8b5cf6;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        border-bottom: 1px solid #1a1a2e;
    }

    .result-body {
        padding: 1.5rem;
        background: #0a0a0f;
        color: #94a3b8;
        font-size: 0.9rem;
        line-height: 1.75;
    }

    .result-body strong {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
    }

    .hint-text {
        font-size: 0.73rem;
        color: #2d3748;
        margin-top: 0.3rem;
        font-style: italic;
        letter-spacing: 0.01em;
    }

    .stSelectbox > div > div {
        background: #0d0d1a !important;
        border-color: #1a1a2e !important;
        color: #94a3b8 !important;
        border-radius: 8px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.85rem !important;
    }

    .stAlert { border-radius: 8px !important; }

    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: #0a0a0f; }
    ::-webkit-scrollbar-thumb { background: #1a1a2e; border-radius: 3px; }

    hr { border-color: #1a1a2e !important; margin: 1.25rem 0 !important; }

    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-brand">ProgressMind</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">AI Daily Assistant</div>', unsafe_allow_html=True)
    st.markdown("---")

    page = st.selectbox(
        "Navigate",
        ["Morning Planner", "Evening Review"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown('<p style="font-size:0.7rem;color:#1e293b;text-align:center;letter-spacing:0.05em;">Gemini AI &nbsp;·&nbsp; Built by Atharva</p>', unsafe_allow_html=True)


# ── Morning Planner ──────────────────────────────────────────────────────────
if page == "Morning Planner":

    st.markdown("""
    <div class="hero">
        <div class="hero-tag">Morning Session</div>
        <div class="hero-title">Plan Your <em>Day</em></div>
        <div class="hero-desc">Drop your tasks, goals, and blockers — I'll build a focused action plan tailored to your day.</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        tasks = st.text_area(
            "Tasks",
            placeholder="Complete DSA problems\nWork on ProgressMind\nRead chapter 3",
            height=140
        )
        st.markdown('<div class="hint-text">One task per line</div>', unsafe_allow_html=True)

    with col2:
        goals = st.text_area(
            "Goals",
            placeholder="Become a backend developer\nFinish semester strong",
            height=140
        )
        st.markdown('<div class="hint-text">What matters most today?</div>', unsafe_allow_html=True)

    blockers = st.text_area(
        "Blockers",
        placeholder="Instagram\nFeeling tired\nWaiting for reply",
        height=100
    )
    st.markdown('<div class="hint-text">What might slow you down?</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Generate Plan"):
        if not tasks.strip():
            st.error("Enter at least one task to continue.")
        else:
            with st.spinner("Building your plan..."):
                try:
                    response = requests.post(f"{API_URL}/morning-plan", json={
                        "tasks":    [t for t in tasks.strip().split("\n") if t.strip()],
                        "goals":    [g for g in goals.strip().split("\n") if g.strip()],
                        "blockers": [b for b in blockers.strip().split("\n") if b.strip()]
                    })
                    if response.status_code == 200:
                        plan = response.json()["plan"]
                        st.markdown('<div class="result-wrap"><div class="result-header">Your Plan</div><div class="result-body">', unsafe_allow_html=True)
                        st.markdown(plan)
                        st.markdown('</div></div>', unsafe_allow_html=True)
                    else:
                        st.error(f"Backend returned {response.status_code}. Check your FastAPI server.")
                except Exception:
                    st.error("Cannot reach backend. Make sure FastAPI is running on port 8080.")


# ── Evening Review ───────────────────────────────────────────────────────────
elif page == "Evening Review":

    st.markdown("""
    <div class="hero">
        <div class="hero-tag">Evening Session</div>
        <div class="hero-title">Review Your <em>Day</em></div>
        <div class="hero-desc">Tell me how your day went — I'll analyze your progress and build tomorrow's plan.</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        completed = st.text_area(
            "Completed Tasks",
            placeholder="DSA practice\nProgressMind backend\nRead chapter 3",
            height=140
        )
        st.markdown('<div class="hint-text">What did you actually finish?</div>', unsafe_allow_html=True)

    with col2:
        incomplete = st.text_area(
            "Incomplete Tasks",
            placeholder="College assignment\nEmail reply",
            height=140
        )
        st.markdown('<div class="hint-text">What got left behind?</div>', unsafe_allow_html=True)

    col3, col4 = st.columns(2, gap="medium")

    with col3:
        blockers = st.text_area(
            "New Blockers",
            placeholder="Doomscrolling\nUnexpected meeting",
            height=100
        )
        st.markdown('<div class="hint-text">What got in your way?</div>', unsafe_allow_html=True)

    with col4:
        mood = st.text_input(
            "Mood",
            placeholder="productive, tired, focused, overwhelmed..."
        )
        st.markdown('<div class="hint-text">How are you feeling right now?</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Review Day"):
        if not completed.strip():
            st.error("Enter at least one completed task to continue.")
        else:
            with st.spinner("Analyzing your day..."):
                try:
                    response = requests.post(f"{API_URL}/evening-review", json={
                        "completed_tasks":  [t for t in completed.strip().split("\n") if t.strip()],
                        "incomplete_tasks": [t for t in incomplete.strip().split("\n") if t.strip()],
                        "new_blockers":     [b for b in blockers.strip().split("\n") if b.strip()],
                        "mood": mood
                    })
                    if response.status_code == 200:
                        review = response.json()["review"]
                        st.markdown('<div class="result-wrap"><div class="result-header">Your Review</div><div class="result-body">', unsafe_allow_html=True)
                        st.markdown(review)
                        st.markdown('</div></div>', unsafe_allow_html=True)
                    else:
                        st.error(f"Backend returned {response.status_code}. Check your FastAPI server.")
                except Exception:
                    st.error("Cannot reach backend. Make sure FastAPI is running on port 8080.")