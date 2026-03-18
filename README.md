# 🖋️ TrueSign — Notary Services Management System

A professional Streamlit web application for notary businesses to manage appointments, display services, and handle client inquiries.

## Features

- **Home** — Branded landing page with service overview and contact info
- **Book Appointment** — Full booking form with validation and confirmation
- **My Appointments** — View, search, and cancel appointments (persisted to JSON)
- **Document Checklist** — Per-service checklists of what clients must bring
- **Services & Fees** — Editable fee schedule across all service categories
- **Contact Us** — Contact form, hours, commission details, and social links

## Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Customization

Search for `[...]` placeholders throughout the source files to fill in:
- Phone, email, address
- Notary commission number and expiration
- Fee schedule amounts
- Social media links

## Deployment on Streamlit Community Cloud

1. Push this folder to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Set **Main file path** to `app.py`
4. Deploy — no additional configuration needed
