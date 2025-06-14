import pandas as pd
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, Trainer, TrainingArguments
import coremltools as ct
import os

# Configuration
INPUT_FILE = "data/text_notes/design_text_data.csv"
MODEL_DIR = "models/distilbert_finetuned"
COREML_OUTPUT = "models/ChipDesignLLM.mlmodel"

def prepare_data():
    """Load and preprocess data for LLM fine-tuning."""
    df = pd.read_csv(INPUT_FILE)
    texts = df['note_text'].tolist()
    labels = df['has_optimization'].tolist()
    return texts, labels

def tokenize_data(texts, tokenizer):
    """Tokenize text data."""
    return tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

def main():
    """Fine-tune DistilBERT and convert to CoreML."""
    # Load data
    texts, labels = prepare_data()

    # Initialize tokenizer and model
    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
    model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

    # Tokenize
    encodings = tokenize_data(texts, tokenizer)
    dataset = torch.utils.data.TensorDataset(
        encodings['input_ids'],
        encodings['attention_mask'],
        torch.tensor(labels)
    )

    # Training arguments
    training_args = TrainingArguments(
        output_dir=MODEL_DIR,
        num_train_epochs=3,
        per_device_train_batch_size=8,
        save_strategy="epoch",
        logging_dir=f"{MODEL_DIR}/logs",
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
    )

    # Fine-tune
    trainer.train()

    # Save model
    model.save_pretrained(MODEL_DIR)
    tokenizer.save_pretrained(MODEL_DIR)
    print(f"Model saved to {MODEL_DIR}")

    # Convert to CoreML
    model.eval()
    sample_input = tokenizer("Optimize transistor density for 3nm process.", return_tensors="pt")
    traced_model = torch.jit.trace(model, (sample_input['input_ids'], sample_input['attention_mask']))
    coreml_model = ct.convert(
        traced_model,
        inputs=[
            ct.TensorType(name="input_ids", shape=sample_input['input_ids'].shape),
            ct.TensorType(name="attention_mask", shape=sample_input['attention_mask'].shape)
        ],
        classifier_config=ct.ClassifierConfig(class_labels=[0, 1])
    )
    coreml_model.save(COREML_OUTPUT)
    print(f"CoreML model saved to {COREML_OUTPUT}")

if __name__ == "__main__":
    main()