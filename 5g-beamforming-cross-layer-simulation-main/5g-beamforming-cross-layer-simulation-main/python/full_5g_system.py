import numpy as np
import matplotlib.pyplot as plt
import socket
import json
import threading
import time
class SignalGenerator:
    def __init__(self, freq=10, samples=1000):
        self.freq = freq
        self.samples = samples

    def generate(self):
        t = np.linspace(0, 1, self.samples)
        return np.sin(2 * np.pi * self.freq * t)
class NoiseModel:
    def add_noise(self, signal):
        noise = np.random.normal(0, 0.5, len(signal))
        return signal + noise
class BeamformingEngine:
    def __init__(self, antennas=64):
        self.antennas = antennas

    def compute_weights(self):
        return np.exp(1j * np.linspace(0, np.pi, self.antennas))

    def apply(self, signal, weights):
        output = np.zeros_like(signal)
        for w in weights:
            output += signal * np.real(w)
        return output / len(weights)

class Metrics:
    def calculate_sinr(self, signal):
        power = np.mean(signal**2)
        noise = np.var(signal - np.mean(signal))
        return 10 * np.log10(power / (noise + 1e-6))

    def calculate_throughput(self):
        return np.random.uniform(50, 100)

    def calculate_latency(self):
        return np.random.uniform(1, 10)
class DataLogger:
    def __init__(self):
        self.data = []

    def log(self, sinr, throughput, latency):
        entry = {
            "SINR": float(sinr),
            "Throughput": float(throughput),
            "Latency": float(latency)
        }
        self.data.append(entry)

    def save(self):
        with open("results.json", "w") as f:
            json.dump(self.data, f, indent=4)
class Visualizer:
    def plot_signal(self, signal):
        plt.figure()
        plt.plot(signal)
        plt.title("Beamformed Signal")
        plt.xlabel("Samples")
        plt.ylabel("Amplitude")
        plt.grid()
        plt.show()
class TCPServer:
    def __init__(self, host='localhost', port=5001):
        self.host = host
        self.port = port

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(1)

        print("Server started on port", self.port)

        conn, addr = server.accept()
        print("Connected:", addr)

        system = FullSystem()

        while True:
            data = conn.recv(1024)
            if not data:
                break

            result = system.run_once()
            conn.send(str(result).encode())

        conn.close()
class FullSystem:
    def __init__(self):
        self.generator = SignalGenerator()
        self.noise = NoiseModel()
        self.beamformer = BeamformingEngine()
        self.metrics = Metrics()
        self.logger = DataLogger()
        self.visualizer = Visualizer()

    def run_once(self):
        signal = self.generator.generate()
        noisy_signal = self.noise.add_noise(signal)

        weights = self.beamformer.compute_weights()
        output = self.beamformer.apply(noisy_signal, weights)

        sinr = self.metrics.calculate_sinr(output)
        throughput = self.metrics.calculate_throughput()
        latency = self.metrics.calculate_latency()

        self.logger.log(sinr, throughput, latency)

        return {
            "SINR": sinr,
            "Throughput": throughput,
            "Latency": latency
        }

    def run_simulation(self, iterations=50):
        for _ in range(iterations):
            self.run_once()

        self.logger.save()
        print("Simulation completed and saved.")

    def visualize(self):
        signal = self.generator.generate()
        self.visualizer.plot_signal(signal)
if __name__ == "__main__":
    system = FullSystem()

    # Run simulation
    system.run_simulation()

    # Visualize result
    system.visualize()

    # Optional: Start TCP server
    # server = TCPServer()
    # server.start()
