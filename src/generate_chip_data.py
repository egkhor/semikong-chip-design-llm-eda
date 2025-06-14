import pandas as pd
import numpy as np
import random
import os

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Configuration
N_SAMPLES = 10000
OUTPUT_DIR = "data/tabular"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "chip_design_data.csv")

# Semiconductor attributes
PROCESS_NODES = ['3nm', '5nm', '7nm', '10nm']
DEFECT_TYPES = ['none', 'lithography', 'etching', 'doping']
YIELD_STATUSES = ['high', 'medium', 'low']

def generate_chip_data(has_defect: bool) -> dict:
    """Generate synthetic tabular data for semiconductor chip design."""
    process_node = random.choice(PROCESS_NODES)
    transistor_count = random.randint(1_000_000, 10_000_000) if not has_defect else random.randint(500_000, 15_000_000)
    defect_type = random.choice(DEFECT_TYPES) if has_defect else 'none'
    defect_rate = random.uniform(0.01, 0.1) if has_defect else 0.0
    yield_status = random.choice(YIELD_STATUSES)
    power_efficiency = random.uniform(0.5, 2.0) if not has_defect else random.uniform(0.3, 1.5)
    fabrication_time = random.randint(10, 50) if not has_defect else random.randint(40, 100)

    return {
        'chip_id': f'CHIP_{random.randint(1000, 9999)}',
        'process_node': process_node,
        'transistor_count': transistor_count,
        'defect_type': defect_type,
        'defect_rate': defect_rate,
        'yield_status': yield_status,
        'power_efficiency': power_efficiency,
        'fabrication_time': fabrication_time,
        'has_defect': int(has_defect)
    }

def main():
    """Generate synthetic chip design dataset and save to CSV."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    data = {
        'chip_id': [],
        'process_node': [],
        'transistor_count': [],
        'defect_type': [],
        'defect_rate': [],
        'yield_status': [],
        'power_efficiency': [],
        'fabrication_time': [],
        'has_defect': []
    }

    for _ in range(N_SAMPLES):
        has_defect = random.choice([True, False])
        chip_data = generate_chip_data(has_defect)
        for key in chip_data:
            data[key].append(chip_data[key])

    df = pd.DataFrame(data)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Tabular dataset generated and saved to {OUTPUT_FILE}")
    print(df.head())

if __name__ == "__main__":
    main()