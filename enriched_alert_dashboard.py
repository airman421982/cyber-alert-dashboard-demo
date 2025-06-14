
import streamlit as st
import pandas as pd
import json

# Load enriched alert data
def load_data():
    with open("enriched_alerts.json", "r") as f:
        data = json.load(f)
    return pd.DataFrame(data)

# Main Streamlit App
st.title("Cyber Alert Enrichment Dashboard")
df = load_data()

# Filter by Risk Score
risk_filter = st.slider("Minimum Risk Score to Display", 1, 5, 3)
filtered_df = df[df['risk_score'] >= risk_filter]

# Show alert table
st.subheader("Filtered Alerts")
st.dataframe(filtered_df)

# Show counts by alert type
st.subheader("Alert Types Breakdown")
st.bar_chart(filtered_df['alert_type'].value_counts())

# Show IP reputation distribution
st.subheader("IP Reputation Distribution")
st.bar_chart(filtered_df['ip_reputation'].value_counts())
