import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Acad Scholarship Calculator",
    layout="centered"
)

# ---------------- Clean Minimal CSS ----------------
st.markdown("""
<style>
    html, body, .stApp {
        background-color: #ffffff;
        color: #111827;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial;
    }

    .block-container {
        max-width: 860px;
        padding-top: 40px;
    }

    h1 {
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 6px;
        color: #111827;
    }

    .subtitle {
        color: #6b7280;
        font-size: 15px;
        margin-bottom: 28px;
    }

    .bucket-title {
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 2px;
        color: #111827;
    }

    .bucket-desc {
        font-size: 14px;
        color: #6b7280;
        margin-bottom: 8px;
    }

    .result-card {
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 28px;
        text-align: center;
        margin-top: 32px;
        background: #ffffff;
    }

    .score {
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 8px;
        color: #111827;
    }

    .scholarship {
        font-size: 16px;
        font-weight: 500;
        color: #374151;
    }

    header, footer {
        visibility: hidden;
        height: 0;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- Data ----------------
OPTIONS = {
    "tenth": {
        "Below 40%": 2,
        "40% – 54%": 4,
        "55% – 69%": 6,
        "70% – 84%": 8,
        "85% and above": 10,
    },
    "graduation": {
        "8.5 and above": 10,
        "7.0 – 8.49": 8,
        "6.0 – 6.99": 6,
        "5.0 – 6.49": 4,
        "Below 5.0": 2,
    },
    "learner": {
        "Fresher": 10,
        "Upskiller ( Currently working in tech and looking to upskill in data. )": 6,
        "Super Upskiller ( Currently working in Data and wants to upskill. )": 8,
        "Unemployed": 4,
        "Switcher ( Currently working in a different field and looking to switch to data. )": 2,
    },
    "background": {
        "CSIT": 5,
        "STEM": 3,
        "Non-STEM": 2,
    },
    "persona": {
        "Moonshot / 29+ Moonshot": 10,
        "Excellent": 9,
        "Good": 8,
        "29+ Excellent": 7,
        "29+ Good": 6,
        "Average": 5,
        "Weak": 4,
        "29+ Average": 3,
        "29+ Weak": 1,
    },
}

# ---------------- Scholarship Logic ----------------
def scholarship_label(score: int) -> str:
    if score <= 33:
        return "No Scholarship — Weak Placeability"
    if score <= 37:
        return "No Scholarship — Average Placeability"
    if score <= 41:
        return "₹10,000 — Good Placeability"
    if score <= 46:
        return "₹20,000 — Excellent Placeability"
    return "₹25,000 — Moonshot Placeability"

# ---------------- Header ----------------
st.markdown("<h1>Acad Scholarship Calculator</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Scholarship is auto-calculated based on predefined buckets.</div>",
    unsafe_allow_html=True
)

# ---------------- Inputs ----------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='bucket-title'>10th Marks (Bucket)</div>", unsafe_allow_html=True)
    st.markdown("<div class='bucket-desc'>Academic performance in Class 10</div>", unsafe_allow_html=True)
    tenth = st.selectbox("", OPTIONS["tenth"].keys(), key="tenth", label_visibility="collapsed")

    st.markdown("<div class='bucket-title'>Graduation Score (Bucket)</div>", unsafe_allow_html=True)
    st.markdown("<div class='bucket-desc'>Undergraduate academic performance</div>", unsafe_allow_html=True)
    graduation = st.selectbox("", OPTIONS["graduation"].keys(), key="graduation", label_visibility="collapsed")

    st.markdown("<div class='bucket-title'>Background (Bucket)</div>", unsafe_allow_html=True)
    st.markdown("<div class='bucket-desc'>Educational background & prior exposure</div>", unsafe_allow_html=True)
    background = st.selectbox("", OPTIONS["background"].keys(), key="background", label_visibility="collapsed")

with col2:
    st.markdown("<div class='bucket-title'>12th Marks (Bucket)</div>", unsafe_allow_html=True)
    st.markdown("<div class='bucket-desc'>Academic performance in Class 12</div>", unsafe_allow_html=True)
    twelfth = st.selectbox("", OPTIONS["tenth"].keys(), key="twelfth", label_visibility="collapsed")

    st.markdown("<div class='bucket-title'>Current Career Status (Bucket)</div>", unsafe_allow_html=True)
    st.markdown("<div class='bucket-desc'>Current professional / career stage</div>", unsafe_allow_html=True)
    learner = st.selectbox("", OPTIONS["learner"].keys(), key="learner", label_visibility="collapsed")

    st.markdown("<div class='bucket-title'>Persona (Bucket)</div>", unsafe_allow_html=True)
    st.markdown("<div class='bucket-desc'>Communication, aptitude & technical</div>", unsafe_allow_html=True)
    persona = st.selectbox("", OPTIONS["persona"].keys(), key="persona", label_visibility="collapsed")

# ---------------- Real-time Calculation ----------------
total_score = (
    OPTIONS["tenth"][tenth]
    + OPTIONS["tenth"][twelfth]
    + OPTIONS["graduation"][graduation]
    + OPTIONS["learner"][learner]
    + OPTIONS["background"][background]
    + OPTIONS["persona"][persona]
)

# ---------------- Result ----------------
st.markdown(
    f"""
    <div class="result-card">
        <div class="score">{total_score}</div>
        <div class="scholarship">{scholarship_label(total_score)}</div>
    </div>
    """,
    unsafe_allow_html=True
)
