import numpy as np

class SignalProcessor:

    def __init__(self, fs=1000):
        self.fs = fs

    def generate_signal(self, freq=10):
        t = np.linspace(0, 1, self.fs)
        return np.sin(2 * np.pi * freq * t)

    def add_noise(self, signal):
        noise = np.random.normal(0, 0.5, len(signal))
        return signal + noise

    def fft_analysis(self, signal):
        fft_vals = np.fft.fft(signal)
        return np.abs(fft_vals)

    def process(self):
        signal = self.generate_signal()
        noisy = self.add_noise(signal)
        fft_result = self.fft_analysis(noisy)

        return fft_result


if __name__ == "__main__":
    sp = SignalProcessor()
    result = sp.process()
    print("Processed FFT:", result[:10])
