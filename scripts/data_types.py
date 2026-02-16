packet_count = 120          # integer
average_latency = 23.5      # float
total_latency = packet_count * average_latency
average_per_packet = total_latency / packet_count

print("Packet Count:", packet_count)
print("Average Latency:", average_latency)
print("Total Latency:", total_latency)
print("Average per Packet:", average_per_packet)

print("\n--- Data Types ---")
print("Type of packet_count:", type(packet_count))
print("Type of average_latency:", type(average_latency))

# String data types
protocol = "TCP"
source_ip = "192.168.1.10"

# String operations
message = "Protocol used: " + protocol
ip_info = f"Source IP address is {source_ip}"

print("\n--- String Data ---")
print(message)
print(ip_info)

print("Type of protocol:", type(protocol))

# Mixing numbers and strings safely
packet_count_str = str(packet_count)
final_message = "Total packets received: " + packet_count_str

print("\n--- Mixing Types Safely ---")
print(final_message)
