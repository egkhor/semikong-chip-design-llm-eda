import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# Configuration
INPUT_FILE = "data/text_notes/design_text_data.csv"
OUTPUT_FILE = "data/text_notes/processed_design_text_data.csv"

def preprocess_text_data():
    """Preprocess design notes for CoreML training."""
    # Load dataset
    df = pd.read_csv(INPUT_FILE)

    # Extract TF-IDF features
    vectorizer = TfidfVectorizer(max_features=50, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['note_text'])
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=[f"tfidf_{i}" for i in range(tfidf_matrix.shape[1])])

    # Combine with existing features
    processed_df = pd.concat([df, tfidf_df], axis=1)

    # Save processed dataset
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    processed_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Processed dataset saved to {OUTPUT_FILE}")
    print(processed_df.head())

if __name__ == "__main__":
    preprocess_text_data()