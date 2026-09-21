# src/analyze.py
# allben-network-analyzer - ML Anomaly Detection
# Developed by Allben Rakgoale

import os
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest


def generate_demo_data(n=200, seed=42):
    """Generate realistic demo network traffic for cloud deployment."""
    np.random.seed(seed)

    # Normal traffic
    normal_ips = [f"192.168.1.{i}" for i in range(10, 30)]
    normal_data = {
        "Source": np.random.choice(normal_ips, size=n, replace=True),
        "Destination": np.random.choice(
            ["8.8.8.8", "1.1.1.1", "142.250.185.78", "104.16.132.229"],
            size=n, replace=True
        ),
        "Protocol": np.random.choice([6, 17, 1], size=n, p=[0.7, 0.25, 0.05]),
        "Timestamp": np.linspace(0, 60, n),
    }
    df = pd.DataFrame(normal_data)

    # Inject 15 suspicious packets (simulated attack)
    attack_ips = ["185.220.101.5", "45.142.212.61", "89.248.165.74"]
    attack_data = {
        "Source": np.random.choice(attack_ips, size=15, replace=True),
        "Destination": ["192.168.1.10"] * 15,
        "Protocol": [6] * 15,
        "Timestamp": np.random.uniform(0, 60, 15),
    }
    attack_df = pd.DataFrame(attack_data)

    return pd.concat([df, attack_df], ignore_index=True)


def load_traffic_data(csv_file="data/traffic_log.csv"):
    """Load traffic data from CSV or generate demo data if unavailable."""
    if os.path.exists(csv_file):
        try:
            df = pd.read_csv(csv_file)
            if not df.empty:
                return df
        except Exception as e:
            print(f"⚠️ Could not read {csv_file}: {e}")

    print("⚠️ No live data — using demo dataset for cloud deployment.")
    return generate_demo_data()


def detect_anomalies(csv_file="data/traffic_log.csv"):
    """Detect suspicious IPs using Isolation Forest."""
    df = load_traffic_data(csv_file)

    if df.empty:
        return None, df

    ip_counts = df["Source"].value_counts().reset_index()
    ip_counts.columns = ["IP", "Count"]

    model = IsolationForest(contamination=0.1, random_state=42)
    ip_counts["Anomaly"] = model.fit_predict(ip_counts[["Count"]])

    suspicious = ip_counts[ip_counts["Anomaly"] == -1]

    if not suspicious.empty:
        print(f"🚨 {len(suspicious)} suspicious IP(s) detected!")
        return suspicious, df
    else:
        print("✅ Network traffic appears normal.")
        return None, df


if __name__ == "__main__":
    suspicious, df = detect_anomalies()
    if suspicious is not None:
        print(suspicious)
