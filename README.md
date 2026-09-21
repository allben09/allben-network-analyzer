<div align="center">

# 🛡️ allben-network-analyzer

### *Enterprise-Grade Network Traffic Analysis with AI-Powered Anomaly Detection*

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://allben-network-analyzer.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Scapy](https://img.shields.io/badge/Scapy-2.5+-4B8BBE?style=for-the-badge&logo=python&logoColor=white)](https://scapy.net)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](Dockerfile)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

**A production-grade network security platform built by [Allben Rakgoale](https://github.com/allben09) that captures live packets, detects anomalies using Machine Learning, and visualizes threats in real-time through an interactive Streamlit dashboard.**

[🌐 Live Demo](https://allben-network-analyzer.streamlit.app/) · [📊 Architecture](#-architecture) · [🚀 Quick Start](#-quick-start) · [🧠 ML Model](#-ml-model-details) · [📸 Screenshots](#-screenshots)

---

### 🌐 **Try the Live Dashboard**

👉 **[https://allben-network-analyzer.streamlit.app](https://allben-network-analyzer.streamlit.app/)**

> ⚠️ **Cloud Environment Note:** Live packet capture requires root/admin privileges which cloud platforms block by design. The cloud version uses **realistic demo data** to showcase the full ML pipeline and dashboard. Running locally enables **true live packet sniffing**.

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Capabilities](#-key-capabilities)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [How It Works](#-how-it-works)
- [ML Model Details](#-ml-model-details)
- [Detection Capabilities](#-detection-capabilities)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Docker Deployment](#-docker-deployment)
- [Cloud Deployment](#-cloud-deployment)
- [Screenshots](#-screenshots)
- [Metrics & Performance](#-metrics--performance)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🔍 Overview

**allben-network-analyzer** is a production-grade network security framework that combines **live packet sniffing**, **protocol analysis**, and **Machine Learning-based anomaly detection**. Built for cybersecurity professionals, network administrators, and security researchers.

The framework was designed to detect real-world threats such as:
- 🔴 **Port scanning** (SYN flag bursts)
- 🔴 **DDoS patterns** (unusual packet rates)
- 🔴 **ARP spoofing** (duplicate MAC responses)
- 🔴 **ICMP reconnaissance** (ping sweeps)
- 🔴 **Suspicious IP activity** (outlier behavior)

---
## 📸 Screenshots

### 🏠 Dashboard Overview
![Dashboard](screenshots/YOUR-ACTUAL-FILENAME.png)

### 📊 Protocol Distribution
[IMAGE SHOWS HERE]
...
---
## 🎯 Key Capabilities

| Capability | Description |
| :--- | :--- |
| 📡 **Real-Time Packet Capture** | Non-intrusive packet sniffing using Scapy |
| 🔍 **Protocol Analysis** | Deep inspection of TCP, UDP, ICMP, and more |
| 🤖 **ML Anomaly Detection** | Isolation Forest model for identifying suspicious traffic patterns |
| 🎯 **Threat Identification** | Detects port scanning, DDoS patterns, ARP spoofing, and malicious IPs |
| 📊 **Interactive Visualization** | Real-time dashboard with traffic metrics and threat alerts |
| 🐳 **Docker Ready** | One-command containerized deployment |
| ☁️ **Cloud Deployed** | Live on Streamlit Cloud with auto-generated demo data |
| 📥 **CSV Export** | Export captured traffic for offline forensic analysis |
| 🌍 **Environment-Aware** | Auto-detects cloud vs. local and adapts gracefully |

---

## 🏗️ Architecture


