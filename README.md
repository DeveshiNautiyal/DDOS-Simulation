# DDoS Attack Simulation and Analysis

This project demonstrates basic DDoS attack simulations using Python and analyzes the network traffic using Wireshark.

## Attacks Implemented

1. TCP SYN Flood Simulation  
   Generates multiple TCP connection requests to simulate SYN flood behavior.

2. UDP Flood Simulation  
   Sends a large number of UDP packets rapidly without establishing a connection.

## Tools Used

- Python
- Wireshark

## Working

The attacks are performed on localhost (127.0.0.1) to ensure safety.  
Wireshark is used to capture and analyze the traffic, where spikes in packet transmission can be observed during the attack.

## Observations

- TCP attack shows increased connection requests.
- UDP attack shows a sharp spike in packet transmission.
- Network traffic returns to normal after the attack stops.

## Conclusion

The project demonstrates how excessive network traffic can affect system performance and how such behavior can be analyzed using Wireshark.
