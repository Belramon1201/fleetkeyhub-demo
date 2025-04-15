
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="FleetKeyHub: VIN & Key Tracking", layout="centered")

st.title("🚗 FleetKeyHub - Vehicle & Key Entry Form")

with st.form("key_entry_form"):
    st.subheader("Enter or Scan Vehicle Info")
    
    badge_number = st.text_input("Employee Badge Number", max_chars=10)
    name = st.text_input("Employee Name")
    
    vin = st.text_input("VIN Number (17 characters max)", max_chars=17)
    plate = st.text_input("Plate Number (7 characters max)", max_chars=7)
    unit = st.text_input("Unit Number (Optional)")
    
    from_location = st.text_input("From Location")
    to_location = st.text_input("To Location")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    submitted = st.form_submit_button("Submit Entry")
    
    if submitted:
        st.success("✅ Entry Submitted!")
        st.write("### Entry Summary:")
        st.write(f"**Timestamp:** {timestamp}")
        st.write(f"**Badge #:** {badge_number}")
        st.write(f"**Name:** {name}")
        st.write(f"**VIN:** {vin}")
        st.write(f"**Plate #:** {plate}")
        st.write(f"**Unit #:** {unit}")
        st.write(f"**From:** {from_location} → **To:** {to_location}")
