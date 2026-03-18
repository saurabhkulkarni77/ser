import streamlit as st
import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "appointments.json")

def _load():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def _save(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2, default=str)

def get_appointments():
    if "appointments" not in st.session_state:
        st.session_state["appointments"] = _load()
    return st.session_state["appointments"]

def add_appointment(appt: dict):
    appts = get_appointments()
    appt["id"] = f"NS-{len(appts)+1001}"
    appt["created_at"] = datetime.now().isoformat()
    appt["status"] = "Confirmed"
    appts.append(appt)
    _save(appts)
    return appt["id"]

def cancel_appointment(appt_id: str):
    appts = get_appointments()
    for a in appts:
        if a["id"] == appt_id:
            a["status"] = "Cancelled"
    _save(appts)

def get_appointment_by_id(appt_id: str):
    for a in get_appointments():
        if a["id"] == appt_id:
            return a
    return None
