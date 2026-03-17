import socket
import threading

target_ip = "127.0.0.1"
target_port = 8000

def attack():
    for _ in range(50):   # limited requests
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(b"GET / HTTP/1.1\r\n\r\n")
            s.close()
        except:
            pass

threads = []

for i in range(20):   # limited threads
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("TCP attack finished safely")