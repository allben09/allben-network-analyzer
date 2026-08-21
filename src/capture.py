#src/capture.py
# allben-network-analyzer - Packet Sniffer Module
# Developed by Allben Rakgoale

from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
import time

packet_data = []

def process_packet(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        
        # Detect potential threats
        if proto == 6:  # TCP
            if packet[TCP].flags == 2:  # SYN flag (potential scanning)
                print(f"⚠️ ALERT: Potential port scan from {ip_src}")
        elif proto == 1:  # ICMP
            print(f"🔍 Ping detected from {ip_src}")
        
        packet_data.append([ip_src, ip_dst, proto, time.time()])
        df = pd.DataFrame(packet_data, columns=["Source", "Destination", "Protocol", "Timestamp"])
        df.to_csv("data/traffic_log.csv", index=False)

print("🛡️ allben-network-analyzer is now sniffing your network...")
print("🔐 Developed by Allben Rakgoale")
sniff(prn=process_packet, store=0)
