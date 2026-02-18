packet_sizes = [120, 340, 560, 230]
print("Original packet sizes:", packet_sizes)
print("First packet size:", packet_sizes[0])
packet_sizes.append(450)
packet_sizes.remove(230)
print("Modified packet sizes:", packet_sizes)

network_config = ("TCP", 80, "IPv4")
print("\nNetwork configuration:", network_config)
print("Protocol:", network_config[0])

traffic_record = {
    "source_ip": "192.168.1.10",
    "destination_ip": "192.168.1.20",
    "packets": 120
}
print("\nTraffic record:", traffic_record)
print("Source IP:", traffic_record["source_ip"])
traffic_record["packets"] = 150
traffic_record["protocol"] = "TCP"
print("Updated traffic record:", traffic_record)