import sys
import os

# Ensure the app's own directory is on the path so `pages` and `store` are
# importable whether Streamlit runs from this folder or from elsewhere.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st

st.set_page_config(
    page_title="TrueSign Notary Services",
    page_icon="🖋️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Lato:wght@300;400;700&display=swap');

:root {
    --cream:   #faf7f2;
    --parchment: #f2ead8;
    --gold:    #b8922a;
    --gold-lt: #d4a843;
    --navy:    #1a2744;
    --navy-lt: #243560;
    --ink:     #2c2c2c;
    --muted:   #7a7060;
    --border:  #ddd4bb;
    --white:   #ffffff;
    --success: #2d6a4f;
    --error:   #9b2335;
}

html, body, [class*="css"] {
    font-family: 'Lato', sans-serif;
    background-color: var(--cream);
    color: var(--ink);
}

.stApp { background-color: var(--cream); }

/* Sidebar */
div[data-testid="stSidebar"] {
    background: var(--navy);
    border-right: 3px solid var(--gold);
}
div[data-testid="stSidebar"] * { color: var(--cream) !important; }
div[data-testid="stSidebar"] .stRadio label { 
    font-family: 'Lato', sans-serif !important;
    font-size: 0.88rem !important;
    letter-spacing: 0.5px;
}

/* Headings */
h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: var(--navy) !important;
}

/* Buttons */
.stButton > button {
    background: var(--navy);
    color: var(--cream);
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    font-size: 0.82rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    border: 1.5px solid var(--gold);
    border-radius: 2px;
    padding: 0.6rem 2rem;
    transition: all 0.2s;
}
.stButton > button:hover {
    background: var(--gold);
    color: var(--navy);
    border-color: var(--gold);
}

/* Inputs */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div,
.stDateInput > div > div > input,
.stNumberInput > div > div > input {
    background-color: var(--white) !important;
    border: 1px solid var(--border) !important;
    border-radius: 2px !important;
    color: var(--ink) !important;
    font-family: 'Lato', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 2px rgba(184,146,42,0.15) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: transparent;
    border-bottom: 2px solid var(--border);
    gap: 0;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Lato', sans-serif;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--muted);
    border-radius: 0;
    padding: 0.7rem 1.5rem;
    background: transparent;
}
.stTabs [aria-selected="true"] {
    color: var(--navy) !important;
    border-bottom: 3px solid var(--gold) !important;
    background: transparent !important;
}

/* Dataframe */
.stDataFrame { border: 1px solid var(--border); border-radius: 4px; }

/* Divider */
hr { border-color: var(--border) !important; }

/* Success/Error */
.stSuccess { background: rgba(45,106,79,0.1) !important; border-left: 3px solid var(--success) !important; }
.stError   { background: rgba(155,35,53,0.1) !important; border-left: 3px solid var(--error) !important; }
.stWarning { background: rgba(184,146,42,0.1) !important; border-left: 3px solid var(--gold) !important; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar nav ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 1.5rem 0 1rem;">
        <div style="font-size:2rem;">🖋️</div>
        <div style="font-family:'Playfair Display',serif; font-size:1.4rem;
                    font-weight:700; color:#d4a843; line-height:1.2;">TrueSign</div>
        <div style="font-size:0.65rem; letter-spacing:4px; text-transform:uppercase;
                    color:#9a9080; margin-top:2px;">Notary Services</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    page = st.radio(
        "Navigation",
        ["🏛️  Home",
         "📅  Book Appointment",
         "📋  My Appointments",
         "📄  Document Checklist",
         "💼  Services & Fees",
         "📞  Contact Us"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("""
    <div style="font-size:0.72rem; color:#7a7060; text-align:center; line-height:1.8; padding:0 0.5rem;">
        <div style="color:#9a9080; letter-spacing:2px; font-size:0.6rem; 
                    text-transform:uppercase; margin-bottom:0.5rem;">Hours</div>
        Mon–Fri: 9am – 6pm<br>
        Saturday: 10am – 3pm<br>
        Sunday: By appointment
    </div>
    """, unsafe_allow_html=True)

# ── Route pages ───────────────────────────────────────────────────────────────
p = page.split("  ")[-1]

if p == "Home":
    from pages import home; home.show()
elif p == "Book Appointment":
    from pages import book; book.show()
elif p == "My Appointments":
    from pages import appointments; appointments.show()
elif p == "Document Checklist":
    from pages import checklist; checklist.show()
elif p == "Services & Fees":
    from pages import services; services.show()
elif p == "Contact Us":
    from pages import contact; contact.show()
