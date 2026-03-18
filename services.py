import streamlit as st


SERVICES = [
    {
        "category": "Standard Notarizations",
        "items": [
            ("General Notarization (per signature)", "$___", "Acknowledgments, jurats, and copy certifications."),
            ("Oaths & Affirmations", "$___", "Sworn statements, affidavits, and depositions."),
            ("Additional Signatures (same document)", "$___", "Per signer beyond the first."),
        ]
    },
    {
        "category": "Specialty Documents",
        "items": [
            ("Power of Attorney", "$___", "General, limited, durable, or healthcare POA."),
            ("Will / Trust Document", "$___", "Includes coordination with required witnesses."),
            ("Apostille Affidavit Preparation", "$___", "Notarized affidavit for international authentication. Secretary of State fees separate."),
            ("I-9 Verification (per employee)", "$___", "Employment eligibility verification with Form I-9."),
        ]
    },
    {
        "category": "Real Estate & Loan Signings",
        "items": [
            ("Real Estate Closing Package", "$___", "Full closing coordination for buyers, sellers, and refinances."),
            ("Loan Signing Package", "$___", "Mortgage, HELOC, or commercial loan packages."),
            ("Deed / Title Transfer", "$___", "Single-document deed notarization."),
            ("Reverse Mortgage Signing", "$___", "Specialized package for reverse mortgage transactions."),
        ]
    },
    {
        "category": "Mobile Notary Services",
        "items": [
            ("Travel Fee — Local (within 10 miles)", "$___", "We come to your location."),
            ("Travel Fee — Extended (10–25 miles)", "$___", "Additional mileage charge applies."),
            ("Hospital / Care Facility Visit", "$___", "Compassionate service for clients with mobility needs."),
            ("After-Hours / Weekend Premium", "$___", "Appointments outside standard business hours."),
        ]
    },
    {
        "category": "Remote Online Notarization (RON)",
        "items": [
            ("RON Session (per signer)", "$___", "Fully compliant remote notarization via secure video platform."),
            ("RON — Multi-Signer Package", "$___", "Up to 4 signers in one session."),
        ]
    },
]


def show():
    st.markdown("""
    <div style="border-left:4px solid #b8922a; padding-left:1rem; margin-bottom:2rem;">
        <div style="font-family:'Playfair Display',serif; font-size:2rem;
                    font-weight:700; color:#1a2744;">Services &amp; Fees</div>
        <div style="font-size:0.88rem; color:#7a7060; margin-top:0.3rem;">
            Transparent, flat-rate pricing. No hidden charges. Fees confirmed prior to your appointment.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#f2ead8; border:1px solid #ddd4bb; border-left:4px solid #b8922a;
                border-radius:2px; padding:1rem 1.3rem; margin-bottom:2rem;
                font-size:0.87rem; color:#5a5040;">
        💡 <strong>Fee Schedule:</strong> Fees marked <em>$___</em> are to be filled in by the notary.
        State law may set maximum allowable fees per signature — contact us for a quote on your specific documents.
    </div>
    """, unsafe_allow_html=True)

    for group in SERVICES:
        st.markdown(f"""
        <div style="font-family:'Playfair Display',serif; font-size:1.2rem;
                    font-weight:700; color:#1a2744; margin:1.8rem 0 0.8rem;
                    border-bottom:2px solid #b8922a; padding-bottom:0.4rem;">
            {group['category']}
        </div>
        """, unsafe_allow_html=True)

        for service_name, fee, desc in group["items"]:
            st.markdown(f"""
            <div style="background:#fff; border:1px solid #ddd4bb; border-radius:2px;
                        padding:1rem 1.3rem; margin-bottom:0.5rem;
                        display:flex; justify-content:space-between; align-items:flex-start;
                        flex-wrap:wrap; gap:0.5rem;">
                <div style="flex:1; min-width:200px;">
                    <div style="font-weight:700; color:#1a2744; font-size:0.9rem;">{service_name}</div>
                    <div style="font-size:0.82rem; color:#7a7060; margin-top:2px;">{desc}</div>
                </div>
                <div style="font-family:'Playfair Display',serif; font-size:1.1rem;
                            font-weight:700; color:#b8922a; white-space:nowrap;">{fee}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background:#1a2744; border-radius:4px; padding:1.5rem;">
            <div style="font-family:'Playfair Display',serif; font-size:1rem;
                        font-weight:700; color:#d4a843; margin-bottom:0.8rem;">
                💳 Payment Methods
            </div>
            <div style="font-size:0.86rem; color:#b8b0a0; line-height:1.9;">
                • Cash<br>
                • Credit / Debit Card (Visa, Mastercard, Amex)<br>
                • Check (payable to: <em>[Business Name]</em>)<br>
                • Zelle / Venmo<br>
                • Invoice (for title companies &amp; law firms)
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background:#fff; border:1px solid #ddd4bb; border-radius:4px; padding:1.5rem;">
            <div style="font-family:'Playfair Display',serif; font-size:1rem;
                        font-weight:700; color:#1a2744; margin-bottom:0.8rem;">
                📋 Fee Policies
            </div>
            <div style="font-size:0.86rem; color:#7a7060; line-height:1.9;">
                • Payment due at time of service<br>
                • Cancellations with &lt;24 hr notice: rescheduling fee applies<br>
                • No-shows: travel fee charged for mobile visits<br>
                • Re-signing due to client error: standard fee applies<br>
                • Receipts provided upon request
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#f2ead8; border-radius:4px; padding:1.2rem 1.5rem;
                margin-top:1.5rem; font-size:0.84rem; color:#5a5040; text-align:center;">
        Questions about pricing for your specific documents?
        <strong style="color:#1a2744;">Contact us</strong> — we'll provide a quote before you book.
    </div>
    """, unsafe_allow_html=True)
