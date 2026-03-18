import streamlit as st


CHECKLISTS = {
    "General Notarization": {
        "icon": "📝",
        "description": "For most standard notarizations — signatures, copies, oaths, and affirmations.",
        "required": [
            "Valid, unexpired government-issued photo ID (driver's license, passport, or state ID)",
            "The original document(s) to be notarized — do NOT sign beforehand",
            "Any co-signers who must also be present at the time of notarization",
        ],
        "optional": [
            "Witness(es) if required by your document — check with your attorney",
            "Any supporting exhibits or attachments referenced in the document",
        ],
        "tips": "Never sign your document before meeting with the notary. The notary must witness your signature."
    },
    "Real Estate Closing": {
        "icon": "🏠",
        "description": "Deeds, title transfers, and property sale/purchase closings.",
        "required": [
            "Valid photo ID for all parties signing",
            "Purchase agreement or contract",
            "Deed or title documents provided by the title company or attorney",
            "Closing disclosure / settlement statement",
            "Proof of homeowner's insurance (if applicable)",
            "Any payoff statements or lien release documents",
        ],
        "optional": [
            "Survey or property description",
            "HOA documents if the property has an association",
        ],
        "tips": "Review all documents before the closing. Bring certified funds or wire confirmation if payment is required at closing."
    },
    "Loan Signing": {
        "icon": "💳",
        "description": "Mortgage, refinance, HELOC, and commercial loan packages.",
        "required": [
            "Valid photo ID (must match loan application name exactly)",
            "Loan package provided by lender or title company",
            "Voided check or bank info for automatic payment setup (if required)",
        ],
        "optional": [
            "Note or promissory note if provided separately",
            "Right of rescission acknowledgment form",
        ],
        "tips": "Loan packages can be lengthy (100+ pages). Budget 60–90 minutes for your appointment."
    },
    "Power of Attorney": {
        "icon": "⚖️",
        "description": "General, limited, durable, or healthcare power of attorney documents.",
        "required": [
            "Valid photo ID for the principal (person granting authority)",
            "Completed Power of Attorney document — review with your attorney first",
            "Valid ID for any witnesses (witnesses typically required — 2 in most states)",
        ],
        "optional": [
            "Attorney contact information if questions arise about document language",
            "Existing POA being revoked (if applicable)",
        ],
        "tips": "Most states require 2 disinterested witnesses. The agent (person receiving authority) typically cannot serve as a witness."
    },
    "Affidavit / Sworn Statement": {
        "icon": "🔏",
        "description": "Affidavits of identity, residence, support, heirship, and more.",
        "required": [
            "Valid photo ID",
            "Completed and typed (not handwritten) affidavit — do NOT sign beforehand",
            "Any exhibits or supporting documents referenced in the affidavit",
        ],
        "optional": [
            "Attorney letter or case number if connected to legal proceedings",
        ],
        "tips": "Signing an affidavit before a notary is a sworn act — ensure all statements are truthful and accurate."
    },
    "Will / Trust Document": {
        "icon": "📜",
        "description": "Last will and testament, living trust, or testamentary documents.",
        "required": [
            "Valid photo ID for the testator/grantor",
            "The original will or trust document drafted by your attorney",
            "Two disinterested witnesses present at signing (required in most states)",
            "Valid ID for each witness",
        ],
        "optional": [
            "Self-proving affidavit (makes probate easier — recommended)",
            "Pour-over will if a living trust is being signed simultaneously",
        ],
        "tips": "Beneficiaries named in the will should NOT serve as witnesses. Contact your estate planning attorney before your appointment."
    },
    "Apostille Preparation": {
        "icon": "🌐",
        "description": "Authentication of documents for international use under the Hague Convention.",
        "required": [
            "Original document requiring authentication (birth certificate, diploma, etc.)",
            "Valid photo ID",
            "Destination country name — apostille requirements vary by country",
        ],
        "optional": [
            "Certified translation if the document is not in the destination country's language",
            "Cover letter explaining the document's purpose",
        ],
        "tips": "Apostilles are issued by the Secretary of State, not the notary. We prepare and notarize supporting affidavits and guide you through submission."
    },
    "I-9 Verification": {
        "icon": "🗂️",
        "description": "Employment eligibility verification for Form I-9.",
        "required": [
            "List A document: U.S. Passport, Permanent Resident Card, or Employment Authorization Document  — OR —",
            "List B + C documents: Driver's license + Social Security card (or birth certificate)",
            "Completed Section 1 of Form I-9 (completed by employee before appointment)",
        ],
        "optional": [
            "Translator certification if Section 1 was completed with translation assistance",
        ],
        "tips": "All documents must be originals — no photocopies accepted. Documents must be unexpired."
    },
}


def show():
    st.markdown("""
    <div style="border-left:4px solid #b8922a; padding-left:1rem; margin-bottom:2rem;">
        <div style="font-family:'Playfair Display',serif; font-size:2rem;
                    font-weight:700; color:#1a2744;">Document Checklist</div>
        <div style="font-size:0.88rem; color:#7a7060; margin-top:0.3rem;">
            Select your service type to see exactly what to bring to your appointment.
        </div>
    </div>
    """, unsafe_allow_html=True)

    service = st.selectbox(
        "Select Service Type",
        list(CHECKLISTS.keys()),
        label_visibility="collapsed",
    )

    data = CHECKLISTS[service]

    st.markdown(f"""
    <div style="background:#1a2744; border-radius:4px; padding:1.2rem 1.5rem;
                margin:1rem 0 1.5rem; display:flex; align-items:center; gap:1rem;">
        <div style="font-size:2rem;">{data['icon']}</div>
        <div>
            <div style="font-family:'Playfair Display',serif; font-size:1.2rem;
                        font-weight:700; color:#faf7f2;">{service}</div>
            <div style="font-size:0.85rem; color:#9a9080; margin-top:2px;">{data['description']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        <div style="font-family:'Playfair Display',serif; font-weight:700;
                    font-size:1rem; color:#1a2744; margin-bottom:0.8rem;">
            ✅ Required — Must Bring
        </div>""", unsafe_allow_html=True)

        for item in data["required"]:
            st.markdown(f"""
            <div style="display:flex; gap:0.8rem; margin-bottom:0.7rem; align-items:flex-start;
                        background:#fff; border:1px solid #ddd4bb; border-radius:2px; padding:0.8rem;">
                <div style="color:#2d6a4f; font-size:1rem; margin-top:1px;">✓</div>
                <div style="font-size:0.87rem; color:#2c2c2c; line-height:1.5;">{item}</div>
            </div>
            """, unsafe_allow_html=True)

        if data.get("optional"):
            st.markdown("""
            <div style="font-family:'Playfair Display',serif; font-weight:700;
                        font-size:1rem; color:#1a2744; margin:1.2rem 0 0.8rem;">
                📎 Optional — Helpful to Bring
            </div>""", unsafe_allow_html=True)

            for item in data["optional"]:
                st.markdown(f"""
                <div style="display:flex; gap:0.8rem; margin-bottom:0.7rem; align-items:flex-start;
                            background:#faf7f2; border:1px solid #ddd4bb; border-radius:2px; padding:0.8rem;">
                    <div style="color:#b8922a; font-size:1rem; margin-top:1px;">○</div>
                    <div style="font-size:0.87rem; color:#5a5040; line-height:1.5;">{item}</div>
                </div>
                """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background:#f2ead8; border:1px solid #ddd4bb; border-radius:4px;
                    padding:1.5rem; margin-bottom:1rem;">
            <div style="font-family:'Playfair Display',serif; font-weight:700;
                        font-size:1rem; color:#1a2744; margin-bottom:0.8rem;">
                💡 Notary Tip
            </div>
            <div style="font-size:0.87rem; color:#5a5040; line-height:1.7;">
                {data['tips']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background:#1a2744; border-radius:4px; padding:1.5rem;">
            <div style="font-family:'Playfair Display',serif; font-weight:700;
                        font-size:1rem; color:#d4a843; margin-bottom:0.8rem;">
                ⚠️ Universal Requirements
            </div>
            <div style="font-size:0.85rem; color:#b8b0a0; line-height:1.8;">
                These apply to <strong style="color:#faf7f2;">every</strong> appointment:<br><br>
                • Valid, unexpired government-issued photo ID<br>
                • Do NOT pre-sign any documents<br>
                • All required signers must be present<br>
                • Documents must be complete (no blank fields)
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#fff; border:1px solid #ddd4bb; border-radius:4px;
                padding:1.2rem 1.5rem; font-size:0.85rem; color:#7a7060;">
        <strong style="color:#1a2744;">Questions about what to bring?</strong>
        Contact us before your appointment — we're happy to review your specific documents
        and confirm you have everything needed.
    </div>
    """, unsafe_allow_html=True)
