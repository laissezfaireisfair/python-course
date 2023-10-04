import argparse
import numpy as np


def read_list(path: str) -> np.ndarray:
    fin = open(path)
    line = fin.readline()
    return np.array(line.split(' '))


def inject_synthetic(real: np.ndarray, synthetic: np.ndarray, probability: float):
    count_to_change = np.random.binomial(real.size, probability)
    indices = np.random.randint(0, real.size, size=count_to_change)
    real[indices] = synthetic[indices]


def main() -> None:
    parser = argparse.ArgumentParser(description='Mult matrices')
    parser.add_argument('realDataPath', type=str, help='Path to real data file')
    parser.add_argument('syntheticDataPath', type=str, help='Path to synthetic data file')
    parser.add_argument('syntheticProbability', type=float, help='Probability of taking synthetic data')

    args = parser.parse_args()
    real_data_path: str = args.realDataPath
    synthetic_data_path: str = args.syntheticDataPath
    synthetic_probability: float = args.syntheticProbability

    if synthetic_probability < 0 or synthetic_probability > 1:
        print(f'Bad probability: {synthetic_probability}')
        return

    try:
        data = read_list(real_data_path)
        synthetic_data = read_list(synthetic_data_path)
    except Exception as exception:
        print(f'Unable to read input: {exception}')
        return

    try:
        inject_synthetic(data, synthetic_data, synthetic_probability)
    except Exception as exception:
        print(f'Injecting synthetic failed: {exception}')
        return

    print(' '.join(data))


main()
