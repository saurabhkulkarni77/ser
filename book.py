import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import store
from datetime import date, timedelta


SERVICE_OPTIONS = [
    "General Notarization",
    "Real Estate Closing",
    "Loan Signing",
    "Affidavit / Sworn Statement",
    "Power of Attorney",
    "Will / Trust Document",
    "Apostille Preparation",
    "I-9 Verification",
    "Mobile Notary (Travel to Me)",
    "Remote Online Notarization (RON)",
    "Other / Not Sure",
]

TIME_SLOTS = [
    "9:00 AM", "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM",
    "12:00 PM", "12:30 PM", "1:00 PM", "1:30 PM", "2:00 PM", "2:30 PM",
    "3:00 PM", "3:30 PM", "4:00 PM", "4:30 PM", "5:00 PM", "5:30 PM",
]


def show():
    st.markdown("""
    <div style="border-left:4px solid #b8922a; padding-left:1rem; margin-bottom:2rem;">
        <div style="font-family:'Playfair Display',serif; font-size:2rem;
                    font-weight:700; color:#1a2744;">Book an Appointment</div>
        <div style="font-size:0.88rem; color:#7a7060; margin-top:0.3rem;">
            Complete the form below and we'll confirm your appointment within 1 business hour.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Confirmation display
    if st.session_state.get("booking_confirmed"):
        conf = st.session_state["booking_confirmed"]
        st.success(f"✅ Appointment confirmed! Your reference number is **{conf['id']}**")
        st.markdown(f"""
        <div style="background:#fff; border:1px solid #ddd4bb; border-radius:4px;
                    padding:1.5rem; margin-bottom:2rem; max-width:600px;">
            <div style="font-family:'Playfair Display',serif; font-size:1.1rem;
                        font-weight:700; color:#1a2744; margin-bottom:1rem;">
                Booking Summary
            </div>
            <table style="width:100%; font-size:0.88rem; border-collapse:collapse;">
                <tr><td style="color:#7a7060; padding:4px 0; width:140px;">Reference #</td>
                    <td style="font-weight:700; color:#1a2744;">{conf['id']}</td></tr>
                <tr><td style="color:#7a7060; padding:4px 0;">Name</td>
                    <td>{conf['first_name']} {conf['last_name']}</td></tr>
                <tr><td style="color:#7a7060; padding:4px 0;">Service</td>
                    <td>{conf['service']}</td></tr>
                <tr><td style="color:#7a7060; padding:4px 0;">Date</td>
                    <td>{conf['appt_date']}</td></tr>
                <tr><td style="color:#7a7060; padding:4px 0;">Time</td>
                    <td>{conf['appt_time']}</td></tr>
                <tr><td style="color:#7a7060; padding:4px 0;">Location</td>
                    <td>{conf['location_type']}</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Book Another Appointment"):
            del st.session_state["booking_confirmed"]
            st.rerun()
        return

    # ── Form ──────────────────────────────────────────────────────────────────
    with st.form("booking_form", clear_on_submit=False):
        st.markdown("""
        <div style="font-family:'Playfair Display',serif; font-size:1rem;
                    font-weight:700; color:#1a2744; border-bottom:1px solid #ddd4bb;
                    padding-bottom:0.5rem; margin-bottom:1rem;">
            1 — Personal Information
        </div>""", unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            first_name = st.text_input("First Name *", placeholder="Jane")
        with c2:
            last_name = st.text_input("Last Name *", placeholder="Smith")

        c3, c4 = st.columns(2)
        with c3:
            email = st.text_input("Email Address *", placeholder="jane@example.com")
        with c4:
            phone = st.text_input("Phone Number *", placeholder="(555) 000-0000")

        st.markdown("""
        <div style="font-family:'Playfair Display',serif; font-size:1rem;
                    font-weight:700; color:#1a2744; border-bottom:1px solid #ddd4bb;
                    padding-bottom:0.5rem; margin:1.5rem 0 1rem;">
            2 — Service Details
        </div>""", unsafe_allow_html=True)

        service = st.selectbox("Service Type *", SERVICE_OPTIONS)

        doc_count = st.number_input(
            "Number of Documents / Signatures",
            min_value=1, max_value=50, value=1,
            help="Approximate count — final fee confirmed at signing."
        )

        notes = st.text_area(
            "Additional Notes",
            placeholder="Describe any special requirements, document types, or questions...",
            height=100
        )

        st.markdown("""
        <div style="font-family:'Playfair Display',serif; font-size:1rem;
                    font-weight:700; color:#1a2744; border-bottom:1px solid #ddd4bb;
                    padding-bottom:0.5rem; margin:1.5rem 0 1rem;">
            3 — Schedule &amp; Location
        </div>""", unsafe_allow_html=True)

        c5, c6 = st.columns(2)
        min_date = date.today() + timedelta(days=1)
        with c5:
            appt_date = st.date_input("Preferred Date *", min_value=min_date,
                                      value=min_date)
        with c6:
            appt_time = st.selectbox("Preferred Time *", TIME_SLOTS)

        location_type = st.radio(
            "Appointment Location *",
            ["Our Office", "Mobile — Come to Me", "Remote Online Notarization (RON)"],
            horizontal=True
        )

        if location_type == "Mobile — Come to Me":
            mobile_address = st.text_input(
                "Your Address *",
                placeholder="123 Main St, City, State ZIP"
            )
        else:
            mobile_address = ""

        st.markdown("""
        <div style="font-family:'Playfair Display',serif; font-size:1rem;
                    font-weight:700; color:#1a2744; border-bottom:1px solid #ddd4bb;
                    padding-bottom:0.5rem; margin:1.5rem 0 1rem;">
            4 — ID Verification Reminder
        </div>""", unsafe_allow_html=True)

        st.markdown("""
        <div style="background:#f2ead8; border:1px solid #ddd4bb; border-radius:2px;
                    padding:1rem 1.2rem; margin-bottom:1rem; font-size:0.85rem; color:#5a5040;">
            ⚠️ <strong>Important:</strong> All signers must present a <strong>valid, unexpired
            government-issued photo ID</strong> (driver's license, passport, or state ID).
            Failure to bring ID will result in cancellation and a rescheduling fee.
        </div>
        """, unsafe_allow_html=True)

        id_ack = st.checkbox("I understand the ID requirement and will bring valid photo ID.")

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Confirm Appointment →", use_container_width=False)

        if submitted:
            errors = []
            if not first_name.strip(): errors.append("First name is required.")
            if not last_name.strip():  errors.append("Last name is required.")
            if not email.strip() or "@" not in email: errors.append("Valid email is required.")
            if not phone.strip():      errors.append("Phone number is required.")
            if location_type == "Mobile — Come to Me" and not mobile_address.strip():
                errors.append("Please enter your address for mobile service.")
            if not id_ack:
                errors.append("Please acknowledge the ID requirement.")

            if errors:
                for e in errors:
                    st.error(e)
            else:
                appt = {
                    "first_name":    first_name.strip(),
                    "last_name":     last_name.strip(),
                    "email":         email.strip(),
                    "phone":         phone.strip(),
                    "service":       service,
                    "doc_count":     int(doc_count),
                    "notes":         notes.strip(),
                    "appt_date":     str(appt_date),
                    "appt_time":     appt_time,
                    "location_type": location_type,
                    "mobile_address": mobile_address.strip(),
                }
                appt_id = store.add_appointment(appt)
                appt["id"] = appt_id
                st.session_state["booking_confirmed"] = appt
                st.rerun()
