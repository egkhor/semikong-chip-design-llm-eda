import pandas as pd
import numpy as np
import random
import os

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Configuration
N_SAMPLES = 10000
OUTPUT_DIR = "data/text_notes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "design_text_data.csv")

# Categories and keywords
PROCESS_NODES = ['3nm', '5nm', '7nm', '10nm']
OPTIMIZATION_KEYWORDS = ['reduce', 'optimize', 'adjust', 'improve']
NEUTRAL_KEYWORDS = ['review', 'maintain', 'standard']
RECOMMENDATIONS = ['Adjust doping levels.', 'Increase layer thickness.', 'Reduce transistor density.', 'Optimize etching process.']

def generate_design_note(has_optimization: bool) -> dict:
    """Generate synthetic design notes and features."""
    process_node = random.choice(PROCESS_NODES)
    if has_optimization:
        action = random.choice(OPTIMIZATION_KEYWORDS)
        note_text = f"{action.capitalize()} {random.choice(['transistor density', 'power efficiency', 'etching parameters'])} for {process_node} process."
        optimization_score = random.uniform(0.7, 1.0)
        has_opt_keyword = 1
        recommendation = random.choice(RECOMMENDATIONS)
    else:
        action = random.choice(NEUTRAL_KEYWORDS)
        note_text = f"{action.capitalize()} current design for {process_node} process."
        optimization_score = random.uniform(0.0, 0.3)
        has_opt_keyword = 0
        recommendation = "Maintain current design."
    note_id = f"NOTE_{random.randint(1000, 9999)}"
    word_count = len(note_text.split())
    engineer_id = f"ENG{random.randint(1000, 9999)}"

    return {
        'note_id': note_id,
        'note_text': note_text,
        'process_node': process_node,
        'word_count': word_count,
        'optimization_score': optimization_score,
        'has_opt_keyword': has_opt_keyword,
        'recommendation': recommendation,
        'engineer_id': engineer_id,
        'has_optimization': int(has_optimization)
    }

def main():
    """Generate synthetic design notes dataset."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    data = {
        'note_id': [],
        'note_text': [],
        'process_node': [],
        'word_count': [],
        'optimization_score': [],
        'has_opt_keyword': [],
        'recommendation': [],
        'engineer_id': [],
        'has_optimization': []
    }

    for _ in range(N_SAMPLES):
        has_optimization = random.choice([True, False])
        note_data = generate_design_note(has_optimization)
        for key in note_data:
            data[key].append(note_data[key])

    df = pd.DataFrame(data)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Text dataset generated and saved to {OUTPUT_FILE}")
    print(df.head())

if __name__ == "__main__":
    main()