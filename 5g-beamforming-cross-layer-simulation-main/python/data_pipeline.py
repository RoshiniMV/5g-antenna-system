import json
import numpy as np

class DataPipeline:

    def __init__(self):
        self.storage = []

    def collect_data(self):
        data = {
            "sinr": np.random.uniform(10, 30),
            "throughput": np.random.uniform(50, 100),
            "latency": np.random.uniform(1, 10)
        }
        self.storage.append(data)
        return data

    def save_to_file(self):
        with open("results.json", "w") as f:
            json.dump(self.storage, f, indent=4)

    def run(self):
        for _ in range(50):
            self.collect_data()
        self.save_to_file()


if __name__ == "__main__":
    dp = DataPipeline()
    dp.run()
