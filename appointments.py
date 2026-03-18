import streamlit as st
import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import store


STATUS_COLORS = {
    "Confirmed": ("#2d6a4f", "#d8f3dc"),
    "Cancelled": ("#9b2335", "#fde8eb"),
    "Completed": ("#1a2744", "#e8edf5"),
}


def badge(status):
    fg, bg = STATUS_COLORS.get(status, ("#555", "#eee"))
    return (f'<span style="background:{bg}; color:{fg}; padding:2px 10px; '
            f'border-radius:20px; font-size:0.72rem; font-weight:700; '
            f'letter-spacing:1px; text-transform:uppercase;">{status}</span>')


def show():
    st.markdown("""
    <div style="border-left:4px solid #b8922a; padding-left:1rem; margin-bottom:2rem;">
        <div style="font-family:'Playfair Display',serif; font-size:2rem;
                    font-weight:700; color:#1a2744;">My Appointments</div>
        <div style="font-size:0.88rem; color:#7a7060; margin-top:0.3rem;">
            View, manage, or cancel your scheduled appointments.
        </div>
    </div>
    """, unsafe_allow_html=True)

    appts = store.get_appointments()

    # ── Lookup by reference or email ─────────────────────────────────────────
    st.markdown("""
    <div style="font-family:'Playfair Display',serif; font-size:1rem; font-weight:700;
                color:#1a2744; margin-bottom:0.8rem;">Look Up an Appointment</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])
    with col1:
        search = st.text_input("Search by Reference # or Email",
                               placeholder="NS-1001  or  jane@example.com",
                               label_visibility="collapsed")
    with col2:
        search_btn = st.button("Search", use_container_width=True)

    if search_btn and search.strip():
        q = search.strip().lower()
        found = [a for a in appts
                 if q in a.get("id", "").lower() or q in a.get("email", "").lower()]

        if not found:
            st.warning("No appointments found matching that reference or email.")
        else:
            for a in found:
                _render_appt_card(a)
        return

    # ── All appointments table ────────────────────────────────────────────────
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Playfair Display',serif; font-size:1rem; font-weight:700;
                color:#1a2744; margin-bottom:0.8rem;">All Scheduled Appointments</div>
    """, unsafe_allow_html=True)

    if not appts:
        st.markdown("""
        <div style="text-align:center; padding:3rem; color:#7a7060;">
            <div style="font-size:2.5rem; margin-bottom:0.5rem;">📋</div>
            <div style="font-family:'Playfair Display',serif; font-size:1.1rem;">
                No appointments yet</div>
            <div style="font-size:0.85rem; margin-top:0.3rem;">
                Use the <strong>Book Appointment</strong> page to schedule your first visit.
            </div>
        </div>
        """, unsafe_allow_html=True)
        return

    # Summary metrics
    total     = len(appts)
    confirmed = sum(1 for a in appts if a.get("status") == "Confirmed")
    cancelled = sum(1 for a in appts if a.get("status") == "Cancelled")

    m1, m2, m3 = st.columns(3)
    for col, label, val, color in [
        (m1, "Total Bookings",     total,     "#1a2744"),
        (m2, "Confirmed",          confirmed,  "#2d6a4f"),
        (m3, "Cancelled",          cancelled,  "#9b2335"),
    ]:
        with col:
            st.markdown(f"""
            <div style="background:#fff; border:1px solid #ddd4bb; border-radius:4px;
                        padding:1rem 1.5rem; text-align:center; margin-bottom:1rem;">
                <div style="font-size:1.8rem; font-weight:700; color:{color};">{val}</div>
                <div style="font-size:0.75rem; text-transform:uppercase; letter-spacing:2px;
                            color:#7a7060;">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    # Filter
    status_filter = st.selectbox("Filter by status", ["All", "Confirmed", "Cancelled", "Completed"])
    filtered = appts if status_filter == "All" else [a for a in appts if a.get("status") == status_filter]

    for a in reversed(filtered):
        _render_appt_card(a)


def _render_appt_card(a):
    status = a.get("status", "Confirmed")
    fg, bg = STATUS_COLORS.get(status, ("#555", "#eee"))

    with st.container():
        st.markdown(f"""
        <div style="background:#fff; border:1px solid #ddd4bb; border-radius:4px;
                    padding:1.2rem 1.5rem; margin-bottom:0.8rem;
                    border-left:4px solid {'#b8922a' if status=='Confirmed' else '#ccc'};">
            <div style="display:flex; justify-content:space-between; align-items:flex-start;
                        flex-wrap:wrap; gap:0.5rem;">
                <div>
                    <div style="font-family:'Playfair Display',serif; font-weight:700;
                                font-size:1rem; color:#1a2744;">
                        {a.get('first_name','')} {a.get('last_name','')}
                        &nbsp;
                        <span style="font-family:'Lato',sans-serif; font-size:0.78rem;
                                     color:#7a7060; font-weight:400;">
                            {a.get('id','')}
                        </span>
                    </div>
                    <div style="font-size:0.85rem; color:#7a7060; margin-top:2px;">
                        📅 {a.get('appt_date','')} at {a.get('appt_time','')} &nbsp;|&nbsp;
                        📄 {a.get('service','')} &nbsp;|&nbsp;
                        📍 {a.get('location_type','')}
                    </div>
                    <div style="font-size:0.83rem; color:#7a7060; margin-top:2px;">
                        ✉️ {a.get('email','')} &nbsp;|&nbsp; 📞 {a.get('phone','')}
                    </div>
                </div>
                <div style="background:{bg}; color:{fg}; padding:4px 12px;
                            border-radius:20px; font-size:0.72rem; font-weight:700;
                            letter-spacing:1px; text-transform:uppercase; white-space:nowrap;">
                    {status}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if status == "Confirmed":
            if st.button(f"Cancel Appointment {a['id']}", key=f"cancel_{a['id']}",
                         type="secondary"):
                store.cancel_appointment(a["id"])
                st.success(f"Appointment {a['id']} has been cancelled.")
                st.rerun()
