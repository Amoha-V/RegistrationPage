import streamlit as st

# Title
st.title("🚀 Team Registration")

# Hardcoded team-to-set mapping
team_assignments = {
    "TeamA": {"api": "https://chronovoyage-api.onrender.com/mars", "interface": "Terminal Window"},
    "TeamB": {"api": "https://chronovoyage-api.onrender.com/ignition", "interface": "Computer Desktop"},
    "TeamC": {"api": "https://chronovoyage-api.onrender.com/frost", "interface": "Smart Phone"},
    "TeamD": {"api": "https://chronovoyage-api.onrender.com/mars", "interface": "Terminal Window"},
    "TeamE": {"api": "https://chronovoyage-api.onrender.com/ignition", "interface": "Computer Desktop"},
    "Amoha": {"api": "https://chronovoyage-api.onrender.com/frost", "interface": "Smart Phone"},
    # Add more teams here...
}

# Input box for team name
team_name = st.text_input("Enter Your Team Name")

# Submit button
if st.button("Register"):
    if team_name.strip() in team_assignments:
        assignment = team_assignments[team_name.strip()]
        st.success(f"✅ **{team_name}**, you have been assigned:")
        st.markdown(f"- **API:** `{assignment['api']}`")
        st.markdown(f"- **Interface:** {assignment['interface']}")
    else:
        st.error("❌ Team name not found. Please check spelling.")
