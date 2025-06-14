# SemiKong Chip Design True LLM with EDA Tool Integration

An open-source AI/ML project to optimize semiconductor chip design using a fine-tuned LLM (DistilBERT) and EDA tool integration. Predicts defects with tabular data, analyzes design notes, and validates via Synopsys API, deployable on iOS/macOS with CoreML.

## Features
- **LLM Analysis**: Fine-tuned DistilBERT classifies design notes and generates recommendations.
- **Defect Prediction**: Classifies chips as defective using tabular data.
- **EDA Integration**: Validates designs with Synopsys API metrics (power, area, timing).
- **Synthetic Datasets**: 10,000 samples each for tabular and text data.
- **CoreML Ready**: Lightweight models for iOS apps.
- **Community-Driven**: Contribute data, models, or Swift code.

## Project Structure
```
semikong-chip-design-llm/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── CONTRIBUTING.md
├── src/
│   ├── generate_chip_data.py
│   ├── generate_text_data.py
│   ├── fine_tune_llm.py
│   ├── eda_integration.py
└── data/
    ├── tabular/
    │   └── chip_design_data.csv
    └── text_notes/
        └── design_text_data.csv
```

## Getting Started
### Prerequisites
- Python 3.8+
- Xcode 13+ with CreateML
- macOS
- Synopsys API key (for EDA integration)
- PyTorch, Transformers, coremltools

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/egkhor/semikong-chip-design-llm.git
   cd semikong-chip-design-llm
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Generate datasets:
   ```bash
   python src/generate_chip_data.py
   python src/generate_text_data.py
   ```
4. Fine-tune LLM:
   ```bash
   python src/fine_tune_llm.py
   ```
5. Run EDA integration (requires API key):
   ```bash
   export SYNOPSYS_API_KEY=your_key
   python src/eda_integration.py
   ```

### Using with CoreML
1. Open Xcode > CreateML > Tabular Classifier for `chip_design_data.csv` (target: `has_defect`).
2. Use `ChipDesignLLM.mlmodel` for text analysis in SwiftUI apps.
3. Integrate EDA metrics from `eda_validated_data.csv`.

## Notes
- **Synthetic Data**: For prototyping; use real data for production.
- **EDA Access**: Requires Synopsys license.
- **Scalability**: Adjust `N_SAMPLES` in scripts.
- **Future Work**: Explore larger LLMs or Cadence integration.

## Contributing
See [CONTRIBUTING.md]([CONTRIBUTING.markdown]).

## License
MIT License. See [LICENSE](LICENSE).

## Contact
Connect via GitHub Issues or www.egkhor.com.my
