import socket
import numpy as np
import threading
import time

# Generate signal
def generate_signal(freq=10, duration=1, fs=1000):
    t = np.linspace(0, duration, fs)
    signal = np.sin(2 * np.pi * freq * t)
    return signal

# Beamforming weights
def generate_weights(n=64):
    return np.exp(1j * np.linspace(0, np.pi, n))

# Apply beamforming
def beamform(signal, weights):
    output = []
    for w in weights:
        output.append(signal * np.real(w))
    return np.sum(output, axis=0)

# Performance metrics
def calculate_metrics(signal):
    power = np.mean(signal**2)
    noise = np.var(signal - np.mean(signal))
    sinr = 10 * np.log10(power / (noise + 1e-6))
    return sinr

# TCP Server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 4000))
    server.listen(1)
  print("Python Beamforming Server Running...")
conn, addr = server.accept()
    print("Connected:", addr)
while True:
data = conn.recv(1024)
if not data:
  break
signal = generate_signal()
weights = generate_weights()
output = beamform(signal, weights)
sinr = calculate_metrics(output)
response = f"SINR:{sinr:.2f}"
conn.send(response.encode())
conn.close()

if __name__ == "__main__":
    start_server()
