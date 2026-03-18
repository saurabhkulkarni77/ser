import streamlit as st


def show():
    # Hero
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1a2744 0%, #243560 100%);
                padding: 4rem 3rem; border-radius: 4px; margin-bottom: 2.5rem;
                border-bottom: 4px solid #b8922a; position: relative; overflow: hidden;">
        <div style="position:absolute; top:-40px; right:-40px; width:200px; height:200px;
                    border-radius:50%; background:rgba(184,146,42,0.08);"></div>
        <div style="position:absolute; bottom:-60px; left:30%; width:300px; height:300px;
                    border-radius:50%; background:rgba(184,146,42,0.05);"></div>
        <div style="font-family:'Playfair Display',serif; font-size:0.7rem;
                    letter-spacing:5px; text-transform:uppercase; color:#b8922a;
                    margin-bottom:0.8rem;">Certified &amp; Commissioned</div>
        <div style="font-family:'Playfair Display',serif; font-size:2.8rem;
                    font-weight:900; color:#faf7f2; line-height:1.15; margin-bottom:1rem;">
            Professional<br>Notary Services<br>
            <span style="color:#d4a843;">You Can Trust</span>
        </div>
        <div style="font-family:'Lato',sans-serif; font-size:1rem; color:#b8b0a0;
                    max-width:520px; line-height:1.7; margin-bottom:1.8rem;">
            Certified notarization for legal documents, real estate closings,
            loan signings, affidavits, and more — fast, accurate, and convenient.
        </div>
        <div style="display:flex; gap:1rem; flex-wrap:wrap;">
            <div style="background:#b8922a; color:#1a2744; padding:0.65rem 2rem;
                        font-family:'Lato',sans-serif; font-weight:700; font-size:0.8rem;
                        letter-spacing:2px; text-transform:uppercase; border-radius:2px;">
                Book an Appointment →
            </div>
            <div style="border:1.5px solid #b8922a; color:#d4a843; padding:0.65rem 2rem;
                        font-family:'Lato',sans-serif; font-weight:700; font-size:0.8rem;
                        letter-spacing:2px; text-transform:uppercase; border-radius:2px;">
                View Services
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Services strip
    st.markdown("""
    <div style="font-family:'Playfair Display',serif; font-size:1.5rem;
                font-weight:700; color:#1a2744; margin-bottom:0.3rem;">
        Our Core Services
    </div>
    <div style="width:50px; height:3px; background:#b8922a; margin-bottom:1.5rem;"></div>
    """, unsafe_allow_html=True)

    services = [
        ("⚖️", "Legal Documents", "Wills, trusts, powers of attorney, affidavits, and sworn statements."),
        ("🏠", "Real Estate", "Deeds, mortgage documents, title transfers, and closing packages."),
        ("✍️", "Loan Signings", "Refinancing, HELOCs, reverse mortgages, and commercial loans."),
        ("🌐", "Apostille", "Authentication for international use — federal and state-level."),
        ("🚗", "Mobile Notary", "We travel to your home, office, hospital, or care facility."),
        ("🔒", "I-9 Verification", "Employment eligibility and identity document verification."),
    ]

    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(services):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="background:#ffffff; border:1px solid #ddd4bb; border-top:3px solid #b8922a;
                        padding:1.5rem; border-radius:2px; margin-bottom:1rem; min-height:160px;">
                <div style="font-size:1.8rem; margin-bottom:0.6rem;">{icon}</div>
                <div style="font-family:'Playfair Display',serif; font-weight:700;
                            font-size:1rem; color:#1a2744; margin-bottom:0.4rem;">{title}</div>
                <div style="font-size:0.85rem; color:#7a7060; line-height:1.6;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Why choose us
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        <div style="font-family:'Playfair Display',serif; font-size:1.5rem;
                    font-weight:700; color:#1a2744; margin-bottom:0.3rem;">
            Why Choose TrueSign?
        </div>
        <div style="width:50px; height:3px; background:#b8922a; margin-bottom:1.5rem;"></div>
        """, unsafe_allow_html=True)

        reasons = [
            ("✓", "State Commissioned & Bonded", "Fully licensed with errors & omissions insurance."),
            ("✓", "Same-Day Appointments Available", "Urgent signings accommodated whenever possible."),
            ("✓", "Mobile & Remote Options", "In-person, travel-to-you, or RON (Remote Online Notarization)."),
            ("✓", "Strict Confidentiality", "Your documents and personal details are never shared."),
            ("✓", "Transparent Pricing", "Flat fees posted upfront — no hidden charges."),
        ]
        for check, title, desc in reasons:
            st.markdown(f"""
            <div style="display:flex; gap:1rem; margin-bottom:1rem; align-items:flex-start;">
                <div style="background:#b8922a; color:#fff; width:22px; height:22px; border-radius:50%;
                            display:flex; align-items:center; justify-content:center;
                            font-size:0.75rem; font-weight:900; flex-shrink:0; margin-top:2px;">{check}</div>
                <div>
                    <div style="font-weight:700; color:#1a2744; font-size:0.9rem;">{title}</div>
                    <div style="font-size:0.83rem; color:#7a7060;">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background:#1a2744; border-radius:4px; padding:2rem;
                    border: 1px solid #b8922a; text-align:center;">
            <div style="font-family:'Playfair Display',serif; font-size:0.7rem;
                        letter-spacing:4px; text-transform:uppercase; color:#b8922a;
                        margin-bottom:1rem;">Quick Contact</div>
            <div style="font-size:2rem; margin-bottom:0.5rem;">📞</div>
            <div style="font-family:'Playfair Display',serif; font-size:1.1rem;
                        color:#faf7f2; margin-bottom:0.3rem;">Phone</div>
            <div style="font-size:0.9rem; color:#9a9080; margin-bottom:1.5rem;">
                [Phone Number]
            </div>
            <div style="font-size:2rem; margin-bottom:0.5rem;">✉️</div>
            <div style="font-family:'Playfair Display',serif; font-size:1.1rem;
                        color:#faf7f2; margin-bottom:0.3rem;">Email</div>
            <div style="font-size:0.9rem; color:#9a9080; margin-bottom:1.5rem;">
                [Email Address]
            </div>
            <div style="font-size:2rem; margin-bottom:0.5rem;">📍</div>
            <div style="font-family:'Playfair Display',serif; font-size:1.1rem;
                        color:#faf7f2; margin-bottom:0.3rem;">Location</div>
            <div style="font-size:0.9rem; color:#9a9080;">
                [Street Address]<br>[City, State ZIP]
            </div>
        </div>
        """, unsafe_allow_html=True)
