import streamlit as st


def show():
    st.markdown("""
    <div style="border-left:4px solid #b8922a; padding-left:1rem; margin-bottom:2rem;">
        <div style="font-family:'Playfair Display',serif; font-size:2rem;
                    font-weight:700; color:#1a2744;">Contact Us</div>
        <div style="font-size:0.88rem; color:#7a7060; margin-top:0.3rem;">
            Reach out with questions or to discuss your notarization needs.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 3])

    with col1:
        # Contact info cards
        cards = [
            ("📞", "Phone", "[Phone Number]", "Call or text during business hours"),
            ("✉️", "Email", "[Email Address]", "Response within 1 business hour"),
            ("📍", "Office Address", "[Street Address]<br>[City, State ZIP]", "In-person appointments available"),
            ("🅿️", "Parking", "[Parking Details]", "Free / validated / street parking"),
        ]

        for icon, label, value, sub in cards:
            st.markdown(f"""
            <div style="background:#fff; border:1px solid #ddd4bb; border-radius:2px;
                        padding:1rem 1.2rem; margin-bottom:0.8rem;
                        display:flex; gap:1rem; align-items:flex-start;">
                <div style="font-size:1.4rem; flex-shrink:0;">{icon}</div>
                <div>
                    <div style="font-size:0.7rem; letter-spacing:3px; text-transform:uppercase;
                                color:#b8922a; font-weight:700;">{label}</div>
                    <div style="font-family:'Playfair Display',serif; font-weight:700;
                                color:#1a2744; font-size:0.95rem; margin:2px 0;">{value}</div>
                    <div style="font-size:0.8rem; color:#7a7060;">{sub}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Hours
        st.markdown("""
        <div style="background:#1a2744; border-radius:4px; padding:1.3rem 1.5rem; margin-top:0.5rem;">
            <div style="font-size:0.7rem; letter-spacing:3px; text-transform:uppercase;
                        color:#b8922a; font-weight:700; margin-bottom:0.8rem;">🕐 Business Hours</div>
            <table style="width:100%; font-size:0.86rem; border-collapse:collapse;">
                <tr><td style="color:#9a9080; padding:3px 0; width:110px;">Monday – Friday</td>
                    <td style="color:#faf7f2; font-weight:700;">9:00 AM – 6:00 PM</td></tr>
                <tr><td style="color:#9a9080; padding:3px 0;">Saturday</td>
                    <td style="color:#faf7f2; font-weight:700;">10:00 AM – 3:00 PM</td></tr>
                <tr><td style="color:#9a9080; padding:3px 0;">Sunday</td>
                    <td style="color:#faf7f2; font-weight:700;">By Appointment Only</td></tr>
                <tr><td style="color:#9a9080; padding:3px 0;">Holidays</td>
                    <td style="color:#faf7f2; font-weight:700;">Closed</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="font-family:'Playfair Display',serif; font-size:1.1rem;
                    font-weight:700; color:#1a2744; margin-bottom:1rem;">
            Send Us a Message
        </div>
        """, unsafe_allow_html=True)

        with st.form("contact_form"):
            c1, c2 = st.columns(2)
            with c1:
                name  = st.text_input("Your Name *", placeholder="Jane Smith")
            with c2:
                email = st.text_input("Email Address *", placeholder="jane@example.com")

            phone = st.text_input("Phone Number", placeholder="(555) 000-0000 (optional)")

            subject = st.selectbox("Subject *", [
                "General Inquiry",
                "Quote Request",
                "Document Question",
                "Appointment Change / Cancellation",
                "Mobile Notary Availability",
                "Remote Online Notarization (RON)",
                "Other",
            ])

            message = st.text_area(
                "Message *",
                placeholder="Describe your notarization needs, ask a question, or request a quote...",
                height=160
            )

            submitted = st.form_submit_button("Send Message →", use_container_width=False)

            if submitted:
                errors = []
                if not name.strip():  errors.append("Name is required.")
                if not email.strip() or "@" not in email: errors.append("Valid email is required.")
                if not message.strip(): errors.append("Message is required.")

                if errors:
                    for e in errors: st.error(e)
                else:
                    st.success(
                        f"✅ Thank you, {name.split()[0]}! Your message has been received. "
                        f"We'll reply to **{email}** within 1 business hour."
                    )

        # Social / extras placeholder
        st.markdown("""
        <div style="background:#f2ead8; border:1px solid #ddd4bb; border-radius:4px;
                    padding:1.3rem 1.5rem; margin-top:1.5rem;">
            <div style="font-family:'Playfair Display',serif; font-size:1rem;
                        font-weight:700; color:#1a2744; margin-bottom:0.8rem;">
                🔗 Find Us Online
            </div>
            <div style="font-size:0.87rem; color:#7a7060; line-height:2;">
                🌐 Website: <span style="color:#b8922a;">[Website URL]</span><br>
                📘 Facebook: <span style="color:#b8922a;">[Facebook Page]</span><br>
                ⭐ Google Reviews: <span style="color:#b8922a;">[Google Business Link]</span><br>
                💼 LinkedIn: <span style="color:#b8922a;">[LinkedIn Profile]</span>
            </div>
        </div>

        <div style="background:#fff; border:1px solid #ddd4bb; border-radius:4px;
                    padding:1.3rem 1.5rem; margin-top:1rem;">
            <div style="font-family:'Playfair Display',serif; font-size:1rem;
                        font-weight:700; color:#1a2744; margin-bottom:0.8rem;">
                🔏 Notary Commission
            </div>
            <div style="font-size:0.87rem; color:#7a7060; line-height:2;">
                Notary Public, State of <span style="color:#1a2744; font-weight:700;">[State]</span><br>
                Commission #: <span style="color:#1a2744; font-weight:700;">[Commission Number]</span><br>
                Commission Expires: <span style="color:#1a2744; font-weight:700;">[Expiration Date]</span><br>
                NNA Certified Signing Agent: <span style="color:#1a2744; font-weight:700;">[Yes / No]</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
