# src/app.py
# allben-network-analyzer - Streamlit Dashboard
# Developed by Allben Rakgoale

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Add src to path so imports work both locally and on Streamlit Cloud
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from analyze import detect_anomalies, load_traffic_data

# ============================================================
# Page config
# ============================================================
st.set_page_config(
    page_title="allben-network-analyzer",
    page_icon="🛡️",
    layout="wide"
)

# ============================================================
# Header
# ============================================================
st.title("🛡️ allben-network-analyzer")
st.caption("Built by Allben Rakgoale | AI-Powered Network Threat Detection")

st.markdown("---")

# ============================================================
# Info banner
# ============================================================
st.info(
    "📡 **Live packet capture** requires root/admin access and only works on a local machine. "
    "This cloud version uses **realistic demo data** to showcase the ML anomaly detection engine. "
    "The full pipeline works identically with live traffic."
)

# ============================================================
# Sidebar
# ============================================================
st.sidebar.header("⚙️ Controls")
uploaded_file = st.sidebar.file_uploader("Upload a CSV of captured traffic", type=["csv"])

use_demo = st.sidebar.checkbox("Use demo dataset", value=True)
if st.sidebar.button("🔄 Refresh Data"):
    st.rerun()

# ============================================================
# Load data
# ============================================================
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("✅ Loaded uploaded file")
elif use_demo:
    df = load_traffic_data(csv_file="nonexistent.csv")  # Forces demo
    st.sidebar.info("Using demo dataset")
else:
    df = load_traffic_data()
    st.sidebar.info("Using local traffic log")

# ============================================================
# Summary metrics
# ============================================================
col1, col2, col3, col4 = st.columns(4)
col1.metric("📦 Total Packets", f"{len(df):,}")
col2.metric("🌐 Unique Sources", df["Source"].nunique())
col3.metric("🎯 Unique Destinations", df["Destination"].nunique())
col4.metric("📡 Protocols", df["Protocol"].nunique())

st.markdown("---")

# ============================================================
# Live traffic table
# ============================================================
st.subheader("📊 Captured Traffic")
st.dataframe(df.head(50), use_container_width=True)

# ============================================================
# Charts
# ============================================================
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📈 Protocol Distribution")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    proto_counts = df["Protocol"].value_counts()
    colors = ["#0F2A4A", "#F5821F", "#0E7C7B"]
    ax1.pie(
        proto_counts,
        labels=[f"Proto {p}" for p in proto_counts.index],
        autopct="%1.1f%%",
        colors=colors[:len(proto_counts)],
        startangle=90
    )
    ax1.axis("equal")
    st.pyplot(fig1)

with col_right:
    st.subheader("🏆 Top 10 Source IPs")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    top_ips = df["Source"].value_counts().head(10)
    sns.barplot(x=top_ips.values, y=top_ips.index, palette="rocket", ax=ax2)
    ax2.set_xlabel("Packet Count")
    ax2.set_ylabel("Source IP")
    st.pyplot(fig2)

# ============================================================
# Anomaly Detection
# ============================================================
st.markdown("---")
st.subheader("🚨 AI-Powered Anomaly Detection")

if st.button("🔍 Run Anomaly Detection Scan"):
    with st.spinner("Analyzing traffic with Isolation Forest..."):
        suspicious, _ = detect_anomalies("nonexistent.csv")

    if suspicious is not None:
        st.error(f"⚠️ {len(suspicious)} suspicious IP(s) detected!")
        st.dataframe(suspicious, use_container_width=True)

        # Bar chart of suspicious IPs
        fig3, ax3 = plt.subplots(figsize=(10, 4))
        sns.barplot(
            data=suspicious, x="IP", y="Count",
            palette="Reds_r", ax=ax3
        )
        ax3.set_title("Suspicious IPs by Packet Count")
        ax3.set_ylabel("Packets")
        ax3.set_xlabel("IP Address")
        plt.xticks(rotation=45)
        st.pyplot(fig3)
    else:
        st.success("✅ No anomalies detected. Network traffic looks normal.")

# ============================================================
# Download button
# ============================================================
st.markdown("---")
st.download_button(
    label="📥 Download Current Traffic Data (CSV)",
    data=df.to_csv(index=False),
    file_name="network_traffic.csv",
    mime="text/csv"
)

# ============================================================
# Footer
# ============================================================
st.markdown("---")
st.caption(
    "🛡️ allben-network-analyzer v1.0 | "
    "Built by [Allben Rakgoale](https://github.com/allben09) | "
    "ML: Isolation Forest"
)
