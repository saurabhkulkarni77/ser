import streamlit as st
import json, os
from datetime import date, timedelta, datetime

st.set_page_config(page_title="TrueSign Notary Services", page_icon="🖋️",
                   layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Lato:wght@300;400;700&display=swap');
:root{--cream:#faf7f2;--parchment:#f2ead8;--gold:#b8922a;--gold-lt:#d4a843;--navy:#1a2744;--ink:#2c2c2c;--muted:#7a7060;--border:#ddd4bb;--white:#ffffff;}
html,body,[class*="css"]{font-family:'Lato',sans-serif;background-color:var(--cream);color:var(--ink);}
.stApp{background-color:var(--cream);}
div[data-testid="stSidebar"]{background:var(--navy);border-right:3px solid var(--gold);}
div[data-testid="stSidebar"] *{color:var(--cream)!important;}
div[data-testid="stSidebar"] .stRadio label{font-family:'Lato',sans-serif!important;font-size:0.88rem!important;}
h1,h2,h3{font-family:'Playfair Display',serif!important;color:var(--navy)!important;}
.stButton>button{background:var(--navy);color:var(--cream);font-family:'Lato',sans-serif;font-weight:700;font-size:0.82rem;letter-spacing:1.5px;text-transform:uppercase;border:1.5px solid var(--gold);border-radius:2px;padding:0.6rem 2rem;transition:all 0.2s;}
.stButton>button:hover{background:var(--gold);color:var(--navy);}
.stTextInput>div>div>input,.stTextArea>div>div>textarea,.stSelectbox>div>div,.stDateInput>div>div>input,.stNumberInput>div>div>input{background-color:var(--white)!important;border:1px solid var(--border)!important;border-radius:2px!important;color:var(--ink)!important;font-family:'Lato',sans-serif!important;}
.stTextInput>div>div>input:focus,.stTextArea>div>div>textarea:focus{border-color:var(--gold)!important;box-shadow:0 0 0 2px rgba(184,146,42,0.15)!important;}
.stTabs [data-baseweb="tab-list"]{background:transparent;border-bottom:2px solid var(--border);gap:0;}
.stTabs [data-baseweb="tab"]{font-family:'Lato',sans-serif;font-size:0.8rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);border-radius:0;padding:0.7rem 1.5rem;background:transparent;}
.stTabs [aria-selected="true"]{color:var(--navy)!important;border-bottom:3px solid var(--gold)!important;background:transparent!important;}
hr{border-color:var(--border)!important;}
</style>""", unsafe_allow_html=True)

# ── DATA STORE ────────────────────────────────────────────────────────────────
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "appointments.json")

def _load():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE) as f: return json.load(f)
        except: pass
    return []

def _save(data):
    try:
        with open(DATA_FILE,"w") as f: json.dump(data, f, indent=2, default=str)
    except: pass  # read-only on Streamlit Cloud — session_state still works

def get_appts():
    if "appointments" not in st.session_state:
        st.session_state["appointments"] = _load()
    return st.session_state["appointments"]

def add_appt(a):
    appts = get_appts()
    a["id"] = f"NS-{1000+len(appts)+1}"
    a["created_at"] = datetime.now().isoformat()
    a["status"] = "Confirmed"
    appts.append(a)
    _save(appts)
    return a["id"]

def cancel_appt(appt_id):
    for a in get_appts():
        if a["id"] == appt_id: a["status"] = "Cancelled"
    _save(get_appts())

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""<div style="text-align:center;padding:1.5rem 0 1rem;">
        <div style="font-size:2rem;">🖋️</div>
        <div style="font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:700;color:#d4a843;line-height:1.2;">TrueSign</div>
        <div style="font-size:0.65rem;letter-spacing:4px;text-transform:uppercase;color:#9a9080;margin-top:2px;">Notary Services</div>
    </div>""", unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio("Nav", ["🏛️  Home","📅  Book Appointment","📋  My Appointments",
                             "📄  Document Checklist","💼  Services & Fees","📞  Contact Us"],
                    label_visibility="collapsed")
    st.markdown("---")
    st.markdown("""<div style="font-size:0.72rem;color:#7a7060;text-align:center;line-height:1.8;padding:0 0.5rem;">
        <div style="color:#9a9080;letter-spacing:2px;font-size:0.6rem;text-transform:uppercase;margin-bottom:0.5rem;">Hours</div>
        Mon–Fri: 9am – 6pm<br>Saturday: 10am – 3pm<br>Sunday: By appointment
    </div>""", unsafe_allow_html=True)

p = page.split("  ")[-1]

# ── HELPERS ───────────────────────────────────────────────────────────────────
def pg_header(title, sub):
    st.markdown(f"""<div style="border-left:4px solid #b8922a;padding-left:1rem;margin-bottom:2rem;">
        <div style="font-family:'Playfair Display',serif;font-size:2rem;font-weight:700;color:#1a2744;">{title}</div>
        <div style="font-size:0.88rem;color:#7a7060;margin-top:0.3rem;">{sub}</div>
    </div>""", unsafe_allow_html=True)

def section_label(n, title):
    st.markdown(f"""<div style="font-family:'Playfair Display',serif;font-size:1rem;font-weight:700;
        color:#1a2744;border-bottom:1px solid #ddd4bb;padding-bottom:0.5rem;margin:1.5rem 0 1rem;">
        {n} — {title}</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════════════════════
if p == "Home":
    st.markdown("""<div style="background:linear-gradient(135deg,#1a2744 0%,#243560 100%);
        padding:4rem 3rem;border-radius:4px;margin-bottom:2.5rem;border-bottom:4px solid #b8922a;
        position:relative;overflow:hidden;">
        <div style="position:absolute;top:-40px;right:-40px;width:200px;height:200px;border-radius:50%;background:rgba(184,146,42,0.08);"></div>
        <div style="font-family:'Playfair Display',serif;font-size:0.7rem;letter-spacing:5px;text-transform:uppercase;color:#b8922a;margin-bottom:0.8rem;">Certified &amp; Commissioned</div>
        <div style="font-family:'Playfair Display',serif;font-size:2.8rem;font-weight:900;color:#faf7f2;line-height:1.15;margin-bottom:1rem;">
            Professional<br>Notary Services<br><span style="color:#d4a843;">You Can Trust</span></div>
        <div style="font-family:'Lato',sans-serif;font-size:1rem;color:#b8b0a0;max-width:520px;line-height:1.7;margin-bottom:1.8rem;">
            Certified notarization for legal documents, real estate closings, loan signings, affidavits, and more — fast, accurate, and convenient.</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:700;color:#1a2744;margin-bottom:0.3rem;">Our Core Services</div>
    <div style="width:50px;height:3px;background:#b8922a;margin-bottom:1.5rem;"></div>""", unsafe_allow_html=True)

    svcs = [("⚖️","Legal Documents","Wills, trusts, powers of attorney, affidavits, and sworn statements."),
            ("🏠","Real Estate","Deeds, mortgage documents, title transfers, and closing packages."),
            ("✍️","Loan Signings","Refinancing, HELOCs, reverse mortgages, and commercial loans."),
            ("🌐","Apostille","Authentication for international use — federal and state-level."),
            ("🚗","Mobile Notary","We travel to your home, office, hospital, or care facility."),
            ("🔒","I-9 Verification","Employment eligibility and identity document verification.")]
    cols = st.columns(3)
    for i,(icon,title,desc) in enumerate(svcs):
        with cols[i%3]:
            st.markdown(f"""<div style="background:#fff;border:1px solid #ddd4bb;border-top:3px solid #b8922a;
                padding:1.5rem;border-radius:2px;margin-bottom:1rem;min-height:160px;">
                <div style="font-size:1.8rem;margin-bottom:0.6rem;">{icon}</div>
                <div style="font-family:'Playfair Display',serif;font-weight:700;font-size:1rem;color:#1a2744;margin-bottom:0.4rem;">{title}</div>
                <div style="font-size:0.85rem;color:#7a7060;line-height:1.6;">{desc}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([3,2])
    with col1:
        st.markdown("""<div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:700;color:#1a2744;margin-bottom:0.3rem;">Why Choose TrueSign?</div>
        <div style="width:50px;height:3px;background:#b8922a;margin-bottom:1.5rem;"></div>""", unsafe_allow_html=True)
        for title,desc in [
            ("State Commissioned & Bonded","Fully licensed with errors & omissions insurance."),
            ("Same-Day Appointments Available","Urgent signings accommodated whenever possible."),
            ("Mobile & Remote Options","In-person, travel-to-you, or RON (Remote Online Notarization)."),
            ("Strict Confidentiality","Your documents and personal details are never shared."),
            ("Transparent Pricing","Flat fees posted upfront — no hidden charges.")]:
            st.markdown(f"""<div style="display:flex;gap:1rem;margin-bottom:1rem;align-items:flex-start;">
                <div style="background:#b8922a;color:#fff;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.75rem;font-weight:900;flex-shrink:0;margin-top:2px;">✓</div>
                <div><div style="font-weight:700;color:#1a2744;font-size:0.9rem;">{title}</div>
                <div style="font-size:0.83rem;color:#7a7060;">{desc}</div></div>
            </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div style="background:#1a2744;border-radius:4px;padding:2rem;border:1px solid #b8922a;text-align:center;">
            <div style="font-family:'Playfair Display',serif;font-size:0.7rem;letter-spacing:4px;text-transform:uppercase;color:#b8922a;margin-bottom:1rem;">Quick Contact</div>
            <div style="font-size:2rem;margin-bottom:0.5rem;">📞</div>
            <div style="font-family:'Playfair Display',serif;font-size:1.1rem;color:#faf7f2;margin-bottom:0.3rem;">Phone</div>
            <div style="font-size:0.9rem;color:#9a9080;margin-bottom:1.5rem;">[Phone Number]</div>
            <div style="font-size:2rem;margin-bottom:0.5rem;">✉️</div>
            <div style="font-family:'Playfair Display',serif;font-size:1.1rem;color:#faf7f2;margin-bottom:0.3rem;">Email</div>
            <div style="font-size:0.9rem;color:#9a9080;margin-bottom:1.5rem;">[Email Address]</div>
            <div style="font-size:2rem;margin-bottom:0.5rem;">📍</div>
            <div style="font-family:'Playfair Display',serif;font-size:1.1rem;color:#faf7f2;margin-bottom:0.3rem;">Location</div>
            <div style="font-size:0.9rem;color:#9a9080;">[Street Address]<br>[City, State ZIP]</div>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# BOOK APPOINTMENT
# ══════════════════════════════════════════════════════════════════════════════
elif p == "Book Appointment":
    pg_header("Book an Appointment", "Complete the form below and we'll confirm within 1 business hour.")

    if st.session_state.get("booking_confirmed"):
        c = st.session_state["booking_confirmed"]
        st.success(f"✅ Appointment confirmed! Reference number: **{c['id']}**")
        st.markdown(f"""<div style="background:#fff;border:1px solid #ddd4bb;border-radius:4px;padding:1.5rem;margin-bottom:2rem;max-width:600px;">
            <div style="font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:700;color:#1a2744;margin-bottom:1rem;">Booking Summary</div>
            <table style="width:100%;font-size:0.88rem;border-collapse:collapse;">
                <tr><td style="color:#7a7060;padding:4px 0;width:140px;">Reference #</td><td style="font-weight:700;color:#1a2744;">{c['id']}</td></tr>
                <tr><td style="color:#7a7060;padding:4px 0;">Name</td><td>{c['first_name']} {c['last_name']}</td></tr>
                <tr><td style="color:#7a7060;padding:4px 0;">Service</td><td>{c['service']}</td></tr>
                <tr><td style="color:#7a7060;padding:4px 0;">Date &amp; Time</td><td>{c['appt_date']} at {c['appt_time']}</td></tr>
                <tr><td style="color:#7a7060;padding:4px 0;">Location</td><td>{c['location_type']}</td></tr>
            </table>
        </div>""", unsafe_allow_html=True)
        if st.button("Book Another Appointment"):
            del st.session_state["booking_confirmed"]
            st.rerun()
    else:
        with st.form("booking_form"):
            section_label("1","Personal Information")
            c1,c2 = st.columns(2)
            with c1: fn = st.text_input("First Name *", placeholder="Jane")
            with c2: ln = st.text_input("Last Name *",  placeholder="Smith")
            c3,c4 = st.columns(2)
            with c3: em = st.text_input("Email Address *", placeholder="jane@example.com")
            with c4: ph = st.text_input("Phone Number *",  placeholder="(555) 000-0000")

            section_label("2","Service Details")
            svc = st.selectbox("Service Type *", ["General Notarization","Real Estate Closing","Loan Signing",
                "Affidavit / Sworn Statement","Power of Attorney","Will / Trust Document",
                "Apostille Preparation","I-9 Verification","Mobile Notary (Travel to Me)",
                "Remote Online Notarization (RON)","Other / Not Sure"])
            doc_count = st.number_input("Number of Documents / Signatures", min_value=1, max_value=50, value=1)
            notes = st.text_area("Additional Notes", placeholder="Describe any special requirements...", height=100)

            section_label("3","Schedule &amp; Location")
            c5,c6 = st.columns(2)
            min_d = date.today() + timedelta(days=1)
            with c5: appt_d = st.date_input("Preferred Date *", min_value=min_d, value=min_d)
            with c6: appt_t = st.selectbox("Preferred Time *", [
                "9:00 AM","9:30 AM","10:00 AM","10:30 AM","11:00 AM","11:30 AM",
                "12:00 PM","12:30 PM","1:00 PM","1:30 PM","2:00 PM","2:30 PM",
                "3:00 PM","3:30 PM","4:00 PM","4:30 PM","5:00 PM","5:30 PM"])
            loc = st.radio("Appointment Location *",
                           ["Our Office","Mobile — Come to Me","Remote Online Notarization (RON)"],
                           horizontal=True)
            mob_addr = ""
            if loc == "Mobile — Come to Me":
                mob_addr = st.text_input("Your Address *", placeholder="123 Main St, City, State ZIP")

            section_label("4","ID Verification Reminder")
            st.markdown("""<div style="background:#f2ead8;border:1px solid #ddd4bb;border-radius:2px;padding:1rem 1.2rem;margin-bottom:1rem;font-size:0.85rem;color:#5a5040;">
                ⚠️ <strong>Important:</strong> All signers must present a <strong>valid, unexpired government-issued photo ID</strong>.
                Failure to bring ID will result in cancellation.</div>""", unsafe_allow_html=True)
            id_ack = st.checkbox("I understand the ID requirement and will bring valid photo ID.")
            st.markdown("<br>", unsafe_allow_html=True)
            submitted = st.form_submit_button("Confirm Appointment →")

            if submitted:
                errs = []
                if not fn.strip(): errs.append("First name is required.")
                if not ln.strip(): errs.append("Last name is required.")
                if not em.strip() or "@" not in em: errs.append("Valid email is required.")
                if not ph.strip(): errs.append("Phone number is required.")
                if loc == "Mobile — Come to Me" and not mob_addr.strip(): errs.append("Please enter your address.")
                if not id_ack: errs.append("Please acknowledge the ID requirement.")
                if errs:
                    for e in errs: st.error(e)
                else:
                    appt = {"first_name":fn.strip(),"last_name":ln.strip(),"email":em.strip(),
                            "phone":ph.strip(),"service":svc,"doc_count":int(doc_count),
                            "notes":notes.strip(),"appt_date":str(appt_d),"appt_time":appt_t,
                            "location_type":loc,"mobile_address":mob_addr.strip()}
                    aid = add_appt(appt)
                    appt["id"] = aid
                    st.session_state["booking_confirmed"] = appt
                    st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# MY APPOINTMENTS
# ══════════════════════════════════════════════════════════════════════════════
elif p == "My Appointments":
    pg_header("My Appointments","View, manage, or cancel your scheduled appointments.")
    appts = get_appts()

    st.markdown("""<div style="font-family:'Playfair Display',serif;font-size:1rem;font-weight:700;color:#1a2744;margin-bottom:0.8rem;">Look Up an Appointment</div>""", unsafe_allow_html=True)
    ca,cb = st.columns([3,1])
    with ca: srch = st.text_input("Search", placeholder="Reference # or email address", label_visibility="collapsed")
    with cb: do_search = st.button("Search", use_container_width=True)

    STATUS_FG = {"Confirmed":"#2d6a4f","Cancelled":"#9b2335","Completed":"#1a2744"}
    STATUS_BG = {"Confirmed":"#d8f3dc","Cancelled":"#fde8eb","Completed":"#e8edf5"}

    def appt_card(a):
        st = a.get("status","Confirmed")
        fg = STATUS_FG.get(st,"#555"); bg = STATUS_BG.get(st,"#eee")
        bl = "#b8922a" if st=="Confirmed" else "#ccc"
        import streamlit as _st
        _st.markdown(f"""<div style="background:#fff;border:1px solid #ddd4bb;border-radius:4px;
            padding:1.2rem 1.5rem;margin-bottom:0.8rem;border-left:4px solid {bl};">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;">
                <div>
                    <div style="font-family:'Playfair Display',serif;font-weight:700;font-size:1rem;color:#1a2744;">
                        {a.get("first_name","")} {a.get("last_name","")}
                        <span style="font-family:'Lato',sans-serif;font-size:0.78rem;color:#7a7060;font-weight:400;">&nbsp;{a.get("id","")}</span></div>
                    <div style="font-size:0.85rem;color:#7a7060;margin-top:2px;">
                        📅 {a.get("appt_date","")} at {a.get("appt_time","")} &nbsp;|&nbsp;
                        📄 {a.get("service","")} &nbsp;|&nbsp; 📍 {a.get("location_type","")}</div>
                    <div style="font-size:0.83rem;color:#7a7060;margin-top:2px;">
                        ✉️ {a.get("email","")} &nbsp;|&nbsp; 📞 {a.get("phone","")}</div>
                </div>
                <div style="background:{bg};color:{fg};padding:4px 12px;border-radius:20px;font-size:0.72rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;white-space:nowrap;">{st}</div>
            </div>
        </div>""", unsafe_allow_html=True)
        if a.get("status") == "Confirmed":
            if _st.button(f"Cancel  {a['id']}", key=f"cancel_{a['id']}"):
                cancel_appt(a["id"])
                _st.success(f"Appointment {a['id']} cancelled.")
                _st.rerun()

    if do_search and srch.strip():
        q = srch.strip().lower()
        found = [a for a in appts if q in a.get("id","").lower() or q in a.get("email","").lower()]
        if not found: st.warning("No appointments found.")
        else: [appt_card(a) for a in found]
    else:
        st.markdown("<hr>", unsafe_allow_html=True)
        if not appts:
            st.markdown("""<div style="text-align:center;padding:3rem;color:#7a7060;">
                <div style="font-size:2.5rem;margin-bottom:0.5rem;">📋</div>
                <div style="font-family:'Playfair Display',serif;font-size:1.1rem;">No appointments yet</div>
                <div style="font-size:0.85rem;margin-top:0.3rem;">Use <strong>Book Appointment</strong> to schedule your first visit.</div>
            </div>""", unsafe_allow_html=True)
        else:
            tot = len(appts); conf = sum(1 for a in appts if a.get("status")=="Confirmed"); canc = sum(1 for a in appts if a.get("status")=="Cancelled")
            for col,label,val,color in zip(st.columns(3),["Total Bookings","Confirmed","Cancelled"],[tot,conf,canc],["#1a2744","#2d6a4f","#9b2335"]):
                with col:
                    st.markdown(f"""<div style="background:#fff;border:1px solid #ddd4bb;border-radius:4px;padding:1rem 1.5rem;text-align:center;margin-bottom:1rem;">
                        <div style="font-size:1.8rem;font-weight:700;color:{color};">{val}</div>
                        <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:2px;color:#7a7060;">{label}</div>
                    </div>""", unsafe_allow_html=True)
            sf = st.selectbox("Filter by status",["All","Confirmed","Cancelled","Completed"])
            filtered = appts if sf=="All" else [a for a in appts if a.get("status")==sf]
            for a in reversed(filtered): appt_card(a)

# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT CHECKLIST
# ══════════════════════════════════════════════════════════════════════════════
elif p == "Document Checklist":
    pg_header("Document Checklist","Select your service type to see exactly what to bring.")

    CHECKLISTS = {
        "General Notarization":{"icon":"📝","description":"Standard notarizations — signatures, copies, oaths, and affirmations.",
            "required":["Valid, unexpired government-issued photo ID","Original document(s) — do NOT sign beforehand","All co-signers must be present"],
            "optional":["Witness(es) if required by your document","Supporting exhibits referenced in the document"],
            "tips":"Never sign your document before meeting with the notary. The notary must witness your signature."},
        "Real Estate Closing":{"icon":"🏠","description":"Deeds, title transfers, and property sale/purchase closings.",
            "required":["Valid photo ID for all parties","Purchase agreement or contract","Deed or title documents from title company","Closing disclosure / settlement statement","Proof of homeowner's insurance (if applicable)","Payoff statements or lien release documents"],
            "optional":["Survey or property description","HOA documents if applicable"],
            "tips":"Review all documents before closing. Bring certified funds or wire confirmation if payment is required."},
        "Loan Signing":{"icon":"💳","description":"Mortgage, refinance, HELOC, and commercial loan packages.",
            "required":["Valid photo ID (must match loan application name exactly)","Loan package from lender or title company","Voided check or bank info if required"],
            "optional":["Promissory note if provided separately","Right of rescission acknowledgment"],
            "tips":"Loan packages can be 100+ pages. Budget 60–90 minutes for your appointment."},
        "Power of Attorney":{"icon":"⚖️","description":"General, limited, durable, or healthcare power of attorney.",
            "required":["Valid photo ID for the principal","Completed POA document — review with attorney first","Valid ID for 2 witnesses (required in most states)"],
            "optional":["Attorney contact info","Existing POA being revoked (if applicable)"],
            "tips":"Most states require 2 disinterested witnesses. The agent (person receiving authority) cannot serve as a witness."},
        "Affidavit / Sworn Statement":{"icon":"🔏","description":"Affidavits of identity, residence, support, heirship, and more.",
            "required":["Valid photo ID","Completed and typed affidavit — do NOT sign beforehand","Any exhibits or supporting documents referenced"],
            "optional":["Attorney letter or case number if connected to legal proceedings"],
            "tips":"Signing an affidavit is a sworn act — ensure all statements are truthful and accurate."},
        "Will / Trust Document":{"icon":"📜","description":"Last will and testament, living trust, or testamentary documents.",
            "required":["Valid photo ID for the testator/grantor","Original will or trust document drafted by attorney","Two disinterested witnesses present at signing","Valid ID for each witness"],
            "optional":["Self-proving affidavit (recommended)","Pour-over will if a living trust is also being signed"],
            "tips":"Beneficiaries named in the will should NOT serve as witnesses. Contact your estate planning attorney first."},
        "Apostille Preparation":{"icon":"🌐","description":"Authentication of documents for international use.",
            "required":["Original document (birth certificate, diploma, etc.)","Valid photo ID","Destination country name"],
            "optional":["Certified translation if required","Cover letter explaining the document's purpose"],
            "tips":"Apostilles are issued by the Secretary of State. We prepare notarized supporting affidavits and guide you through submission."},
        "I-9 Verification":{"icon":"🗂️","description":"Employment eligibility verification for Form I-9.",
            "required":["List A document (U.S. Passport, Permanent Resident Card)  — OR —","List B + C: Driver's license + Social Security card","Completed Section 1 of Form I-9 (employee completes before appointment)"],
            "optional":["Translator certification if Section 1 was completed with assistance"],
            "tips":"All documents must be originals — no photocopies. All documents must be unexpired."},
    }

    svc = st.selectbox("Select Service Type", list(CHECKLISTS.keys()), label_visibility="collapsed")
    d = CHECKLISTS[svc]

    st.markdown(f"""<div style="background:#1a2744;border-radius:4px;padding:1.2rem 1.5rem;margin:1rem 0 1.5rem;display:flex;align-items:center;gap:1rem;">
        <div style="font-size:2rem;">{d['icon']}</div>
        <div><div style="font-family:'Playfair Display',serif;font-size:1.2rem;font-weight:700;color:#faf7f2;">{svc}</div>
        <div style="font-size:0.85rem;color:#9a9080;margin-top:2px;">{d['description']}</div></div>
    </div>""", unsafe_allow_html=True)

    cl1,cl2 = st.columns([3,2])
    with cl1:
        st.markdown("""<div style="font-family:'Playfair Display',serif;font-weight:700;font-size:1rem;color:#1a2744;margin-bottom:0.8rem;">✅ Required — Must Bring</div>""", unsafe_allow_html=True)
        for item in d["required"]:
            st.markdown(f"""<div style="display:flex;gap:0.8rem;margin-bottom:0.7rem;align-items:flex-start;background:#fff;border:1px solid #ddd4bb;border-radius:2px;padding:0.8rem;">
                <div style="color:#2d6a4f;font-size:1rem;margin-top:1px;">✓</div>
                <div style="font-size:0.87rem;color:#2c2c2c;line-height:1.5;">{item}</div>
            </div>""", unsafe_allow_html=True)
        if d.get("optional"):
            st.markdown("""<div style="font-family:'Playfair Display',serif;font-weight:700;font-size:1rem;color:#1a2744;margin:1.2rem 0 0.8rem;">📎 Optional — Helpful to Bring</div>""", unsafe_allow_html=True)
            for item in d["optional"]:
                st.markdown(f"""<div style="display:flex;gap:0.8rem;margin-bottom:0.7rem;align-items:flex-start;background:#faf7f2;border:1px solid #ddd4bb;border-radius:2px;padding:0.8rem;">
                    <div style="color:#b8922a;font-size:1rem;margin-top:1px;">○</div>
                    <div style="font-size:0.87rem;color:#5a5040;line-height:1.5;">{item}</div>
                </div>""", unsafe_allow_html=True)
    with cl2:
        st.markdown(f"""<div style="background:#f2ead8;border:1px solid #ddd4bb;border-radius:4px;padding:1.5rem;margin-bottom:1rem;">
            <div style="font-family:'Playfair Display',serif;font-weight:700;font-size:1rem;color:#1a2744;margin-bottom:0.8rem;">💡 Notary Tip</div>
            <div style="font-size:0.87rem;color:#5a5040;line-height:1.7;">{d['tips']}</div>
        </div>
        <div style="background:#1a2744;border-radius:4px;padding:1.5rem;">
            <div style="font-family:'Playfair Display',serif;font-weight:700;font-size:1rem;color:#d4a843;margin-bottom:0.8rem;">⚠️ Universal Requirements</div>
            <div style="font-size:0.85rem;color:#b8b0a0;line-height:1.8;">
                These apply to <strong style="color:#faf7f2;">every</strong> appointment:<br><br>
                • Valid, unexpired government-issued photo ID<br>
                • Do NOT pre-sign any documents<br>
                • All required signers must be present<br>
                • Documents must be complete (no blank fields)
            </div>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SERVICES & FEES
# ══════════════════════════════════════════════════════════════════════════════
elif p == "Services & Fees":
    pg_header("Services &amp; Fees","Transparent, flat-rate pricing. No hidden charges.")

    st.markdown("""<div style="background:#f2ead8;border:1px solid #ddd4bb;border-left:4px solid #b8922a;border-radius:2px;padding:1rem 1.3rem;margin-bottom:2rem;font-size:0.87rem;color:#5a5040;">
        💡 Fees marked <em>$___</em> are to be filled in by the notary. Contact us for a quote on your specific documents.
    </div>""", unsafe_allow_html=True)

    for cat, items in [
        ("Standard Notarizations",[
            ("General Notarization (per signature)","$___","Acknowledgments, jurats, and copy certifications."),
            ("Oaths & Affirmations","$___","Sworn statements, affidavits, and depositions."),
            ("Additional Signatures (same document)","$___","Per signer beyond the first.")]),
        ("Specialty Documents",[
            ("Power of Attorney","$___","General, limited, durable, or healthcare POA."),
            ("Will / Trust Document","$___","Includes coordination with required witnesses."),
            ("Apostille Affidavit Prep","$___","Notarized affidavit for international authentication. SoS fees separate."),
            ("I-9 Verification (per employee)","$___","Employment eligibility verification.")]),
        ("Real Estate & Loan Signings",[
            ("Real Estate Closing Package","$___","Full closing coordination for buyers, sellers, and refinances."),
            ("Loan Signing Package","$___","Mortgage, HELOC, or commercial loan packages."),
            ("Deed / Title Transfer","$___","Single-document deed notarization."),
            ("Reverse Mortgage Signing","$___","Specialized package for reverse mortgage transactions.")]),
        ("Mobile Notary Services",[
            ("Travel Fee — Local (≤10 miles)","$___","We come to your location."),
            ("Travel Fee — Extended (10–25 mi)","$___","Additional mileage charge applies."),
            ("Hospital / Care Facility Visit","$___","Compassionate service for clients with mobility needs."),
            ("After-Hours / Weekend Premium","$___","Appointments outside standard business hours.")]),
        ("Remote Online Notarization (RON)",[
            ("RON Session (per signer)","$___","Fully compliant remote notarization via secure video platform."),
            ("RON — Multi-Signer Package","$___","Up to 4 signers in one session.")])
    ]:
        st.markdown(f"""<div style="font-family:'Playfair Display',serif;font-size:1.2rem;font-weight:700;color:#1a2744;margin:1.8rem 0 0.8rem;border-bottom:2px solid #b8922a;padding-bottom:0.4rem;">{cat}</div>""", unsafe_allow_html=True)
        for name,fee,desc in items:
            st.markdown(f"""<div style="background:#fff;border:1px solid #ddd4bb;border-radius:2px;padding:1rem 1.3rem;margin-bottom:0.5rem;display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;">
                <div style="flex:1;min-width:200px;">
                    <div style="font-weight:700;color:#1a2744;font-size:0.9rem;">{name}</div>
                    <div style="font-size:0.82rem;color:#7a7060;margin-top:2px;">{desc}</div>
                </div>
                <div style="font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:700;color:#b8922a;white-space:nowrap;">{fee}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    pc1,pc2 = st.columns(2)
    with pc1:
        st.markdown("""<div style="background:#1a2744;border-radius:4px;padding:1.5rem;">
            <div style="font-family:'Playfair Display',serif;font-size:1rem;font-weight:700;color:#d4a843;margin-bottom:0.8rem;">💳 Payment Methods</div>
            <div style="font-size:0.86rem;color:#b8b0a0;line-height:1.9;">• Cash<br>• Credit / Debit Card (Visa, MC, Amex)<br>• Check (payable to: <em>[Business Name]</em>)<br>• Zelle / Venmo<br>• Invoice (title companies &amp; law firms)</div>
        </div>""", unsafe_allow_html=True)
    with pc2:
        st.markdown("""<div style="background:#fff;border:1px solid #ddd4bb;border-radius:4px;padding:1.5rem;">
            <div style="font-family:'Playfair Display',serif;font-size:1rem;font-weight:700;color:#1a2744;margin-bottom:0.8rem;">📋 Fee Policies</div>
            <div style="font-size:0.86rem;color:#7a7060;line-height:1.9;">• Payment due at time of service<br>• Cancellations &lt;24 hr notice: rescheduling fee<br>• No-shows: travel fee charged for mobile visits<br>• Re-signing due to client error: standard fee applies<br>• Receipts provided upon request</div>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════════════════════════════════════
elif p == "Contact Us":
    pg_header("Contact Us","Reach out with questions or to discuss your notarization needs.")

    cc1,cc2 = st.columns([2,3])
    with cc1:
        for icon,label,value,sub in [
            ("📞","Phone","[Phone Number]","Call or text during business hours"),
            ("✉️","Email","[Email Address]","Response within 1 business hour"),
            ("📍","Office Address","[Street Address]<br>[City, State ZIP]","In-person appointments available"),
            ("🅿️","Parking","[Parking Details]","Free / validated / street parking")]:
            st.markdown(f"""<div style="background:#fff;border:1px solid #ddd4bb;border-radius:2px;padding:1rem 1.2rem;margin-bottom:0.8rem;display:flex;gap:1rem;align-items:flex-start;">
                <div style="font-size:1.4rem;flex-shrink:0;">{icon}</div>
                <div><div style="font-size:0.7rem;letter-spacing:3px;text-transform:uppercase;color:#b8922a;font-weight:700;">{label}</div>
                <div style="font-family:'Playfair Display',serif;font-weight:700;color:#1a2744;font-size:0.95rem;margin:2px 0;">{value}</div>
                <div style="font-size:0.8rem;color:#7a7060;">{sub}</div></div>
            </div>""", unsafe_allow_html=True)
        st.markdown("""<div style="background:#1a2744;border-radius:4px;padding:1.3rem 1.5rem;margin-top:0.5rem;">
            <div style="font-size:0.7rem;letter-spacing:3px;text-transform:uppercase;color:#b8922a;font-weight:700;margin-bottom:0.8rem;">🕐 Business Hours</div>
            <table style="width:100%;font-size:0.86rem;border-collapse:collapse;">
                <tr><td style="color:#9a9080;padding:3px 0;width:110px;">Monday – Friday</td><td style="color:#faf7f2;font-weight:700;">9:00 AM – 6:00 PM</td></tr>
                <tr><td style="color:#9a9080;padding:3px 0;">Saturday</td><td style="color:#faf7f2;font-weight:700;">10:00 AM – 3:00 PM</td></tr>
                <tr><td style="color:#9a9080;padding:3px 0;">Sunday</td><td style="color:#faf7f2;font-weight:700;">By Appointment Only</td></tr>
                <tr><td style="color:#9a9080;padding:3px 0;">Holidays</td><td style="color:#faf7f2;font-weight:700;">Closed</td></tr>
            </table>
        </div>""", unsafe_allow_html=True)

    with cc2:
        st.markdown("""<div style="font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:700;color:#1a2744;margin-bottom:1rem;">Send Us a Message</div>""", unsafe_allow_html=True)
        with st.form("contact_form"):
            cf1,cf2 = st.columns(2)
            with cf1: cn = st.text_input("Your Name *",    placeholder="Jane Smith")
            with cf2: ce = st.text_input("Email Address *",placeholder="jane@example.com")
            cp = st.text_input("Phone Number",placeholder="(555) 000-0000 (optional)")
            cs = st.selectbox("Subject *",["General Inquiry","Quote Request","Document Question",
                "Appointment Change / Cancellation","Mobile Notary Availability",
                "Remote Online Notarization (RON)","Other"])
            cm = st.text_area("Message *",placeholder="Describe your notarization needs or ask a question...",height=160)
            csub = st.form_submit_button("Send Message →")
            if csub:
                cerrs=[]
                if not cn.strip(): cerrs.append("Name is required.")
                if not ce.strip() or "@" not in ce: cerrs.append("Valid email is required.")
                if not cm.strip(): cerrs.append("Message is required.")
                if cerrs:
                    for e in cerrs: st.error(e)
                else:
                    st.success(f"✅ Thank you, {cn.split()[0]}! Your message has been received. We'll reply to **{ce}** within 1 business hour.")

        st.markdown("""<div style="background:#f2ead8;border:1px solid #ddd4bb;border-radius:4px;padding:1.3rem 1.5rem;margin-top:1.5rem;">
            <div style="font-family:'Playfair Display',serif;font-size:1rem;font-weight:700;color:#1a2744;margin-bottom:0.8rem;">🔗 Find Us Online</div>
            <div style="font-size:0.87rem;color:#7a7060;line-height:2;">
                🌐 Website: <span style="color:#b8922a;">[Website URL]</span><br>
                📘 Facebook: <span style="color:#b8922a;">[Facebook Page]</span><br>
                ⭐ Google Reviews: <span style="color:#b8922a;">[Google Business Link]</span><br>
                💼 LinkedIn: <span style="color:#b8922a;">[LinkedIn Profile]</span>
            </div>
        </div>
        <div style="background:#fff;border:1px solid #ddd4bb;border-radius:4px;padding:1.3rem 1.5rem;margin-top:1rem;">
            <div style="font-family:'Playfair Display',serif;font-size:1rem;font-weight:700;color:#1a2744;margin-bottom:0.8rem;">🔏 Notary Commission</div>
            <div style="font-size:0.87rem;color:#7a7060;line-height:2;">
                Notary Public, State of <strong style="color:#1a2744;">[State]</strong><br>
                Commission #: <strong style="color:#1a2744;">[Commission Number]</strong><br>
                Commission Expires: <strong style="color:#1a2744;">[Expiration Date]</strong><br>
                NNA Certified Signing Agent: <strong style="color:#1a2744;">[Yes / No]</strong>
            </div>
        </div>""", unsafe_allow_html=True)
