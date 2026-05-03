import socket
import numpy as np
import time
class BeamformingController:
 def __init__(self):
        self.antennas = 64
 def generate_signal(self):
        t = np.linspace(0, 1, 1000)
        return np.sin(2 * np.pi * 10 * t)
 def compute_weights(self):
        return np.exp(1j * np.linspace(0, np.pi, self.antennas))
def beamform(self, signal, weights):
        output = np.zeros_like(signal)
        for w in weights:
            output += signal * np.real(w)
        return output / len(weights)
def calculate_sinr(self, signal):
        power = np.mean(signal**2)
        noise = np.var(signal - np.mean(signal))
        return 10 * np.log10(power / (noise + 1e-6))
def run(self):
        signal = self.generate_signal()
        weights = self.compute_weights()
        output = self.beamform(signal, weights)
        sinr = self.calculate_sinr(output)
       print("Beamforming Completed")
        print("SINR:", sinr)
class TCPServer:
def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
 def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(1)
print("Server started...")
conn, addr = server.accept()
print("Connected:", addr)
 controller = BeamformingController()
while True:
            data = conn.recv(1024)
            if not data:
                break
              controller.run()
            conn.send(b"Processed")
 conn.close()
if __name__ == "__main__":
    TCPServer().start()
