# src/capture.py
# allben-network-analyzer - Packet Sniffer Module
# Developed by Allben Rakgoale
#
# NOTE: Live sniffing requires root/admin access and won't work on
# cloud platforms like Streamlit Cloud. This module is optional.

import os
import time
import pandas as pd

packet_data = []

# Try importing scapy, but don't fail if unavailable
try:
    from scapy.all import sniff, IP, TCP, UDP
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False
    print("⚠️ Scapy not available. Live capture disabled.")


def process_packet(packet):
    """Process each captured packet."""
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        # Detect potential threats
        if proto == 6:  # TCP
            if packet[TCP].flags == 2:  # SYN flag
                print(f"⚠️ ALERT: Potential port scan from {ip_src}")
        elif proto == 1:  # ICMP
            print(f"🔍 Ping detected from {ip_src}")

        packet_data.append([ip_src, ip_dst, proto, time.time()])

        # Save every 10 packets
        if len(packet_data) % 10 == 0:
            os.makedirs("data", exist_ok=True)
            df = pd.DataFrame(
                packet_data,
                columns=["Source", "Destination", "Protocol", "Timestamp"]
            )
            df.to_csv("data/traffic_log.csv", index=False)


def start_capture(interface=None, count=0):
    """Start live packet capture (requires admin/root)."""
    if not SCAPY_AVAILABLE:
        raise RuntimeError("Scapy is not installed or not available.")
    print("🛡️ allben-network-analyzer is now sniffing your network...")
    print("🔐 Developed by Allben Rakgoale")
    sniff(prn=process_packet, store=0, iface=interface, count=count)


if __name__ == "__main__":
    start_capture()
