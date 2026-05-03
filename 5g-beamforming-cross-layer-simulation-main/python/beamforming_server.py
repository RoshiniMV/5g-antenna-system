import socket
import numpy as np
def beamforming(weights, signal):
    return np.dot(weights, signal)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 3000))
server.listen(1)
print("Server running...")
conn, addr = server.accept()
print("Connected:", addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    signal = np.random.rand(10)
    weights = np.random.rand(10)
    output = beamforming(weights, signal)
     conn.send(str(output).encode())
