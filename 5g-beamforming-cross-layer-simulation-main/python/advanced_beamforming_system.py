import numpy as np
import matplotlib.pyplot as plt

class BeamformingSystem:

    def __init__(self, antennas=64):
        self.antennas = antennas
        self.weights = np.ones(antennas)

    def generate_signal(self, freq=10, samples=1000):
        t = np.linspace(0, 1, samples)
        return np.sin(2 * np.pi * freq * t)

    def add_noise(self, signal):
        noise = np.random.normal(0, 0.5, len(signal))
        return signal + noise

    def compute_weights(self):
        self.weights = np.exp(1j * np.linspace(0, np.pi, self.antennas))

    def beamform(self, signal):
        output = np.zeros_like(signal)
        for w in self.weights:
            output += signal * np.real(w)
        return output / self.antennas

    def calculate_sinr(self, signal):
        signal_power = np.mean(signal**2)
        noise_power = np.var(signal - np.mean(signal))
        return 10 * np.log10(signal_power / (noise_power + 1e-6))

    def run(self):
        signal = self.generate_signal()
        noisy = self.add_noise(signal)
        self.compute_weights()
        output = self.beamform(noisy)

        sinr = self.calculate_sinr(output)

        print("SINR:", sinr)

        plt.plot(output)
        plt.title("Beamformed Signal")
        plt.show()


if __name__ == "__main__":
    system = BeamformingSystem()
    system.run()
