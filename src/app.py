# src/app.py
# allben-network-analyzer - Streamlit Dashboard
# Developed by Allben Rakgoale

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from analyze import detect_anomalies

st.set_page_config(page_title="allben-network-analyzer", layout="wide")

st.title("🛡️ allben-network-analyzer")
st.caption("Built by Allben Rakgoale | AI-Powered Threat Detection")
st.markdown("---")

st.markdown("### Real-time Anomaly Detection using Machine Learning")

try:
    df = pd.read_csv("data/traffic_log.csv")
    st.dataframe(df)
    
    st.subheader("📊 Protocol Distribution")
    fig, ax = plt.subplots()
    df['Protocol'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)
    
    if st.button("🔍 Scan for Threats"):
        results = detect_anomalies()
        if results is not None:
            st.warning("🚨 Suspicious IPs Found")
            st.table(results)
        else:
            st.success("✅ No threats detected")
            
except:
    st.warning("No traffic captured yet. Run the sniffer first!")
