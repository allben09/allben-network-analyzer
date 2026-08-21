# src/analyze.py
# allben-network-analyzer - ML Anomaly Detection
# Developed by Allben Rakgoale

import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(csv_file="data/traffic_log.csv"):
    df = pd.read_csv(csv_file)
    
    ip_counts = df['Source'].value_counts().reset_index()
    ip_counts.columns = ['IP', 'Count']
    
    model = IsolationForest(contamination=0.1)
    ip_counts['Anomaly'] = model.fit_predict(ip_counts[['Count']])
    
    suspicious_ips = ip_counts[ip_counts['Anomaly'] == -1]
    
    if not suspicious_ips.empty:
        print("🚨 SUSPICIOUS IP ADDRESSES DETECTED!")
        print(suspicious_ips)
        return suspicious_ips
    else:
        print("✅ Network traffic appears normal.")
        return None
