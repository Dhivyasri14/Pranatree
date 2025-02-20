from datasets import Dataset
from transformers import (
    Trainer, TrainingArguments, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling, pipeline
)
import torch

# Step 1: Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Step 2: Prepare the dataset (formatted as a dictionary)
def prepare_dataset():
    global data
    data = {
        "Tourist places in Paris": "Eiffel Tower, Louvre Museum, Notre-Dame Cathedral",
        "Tourist places in Kerala": "Alleppey, Munnar, Wayanad, Fort Kochi",
        "Tourist places in Rome": "Colosseum, Vatican Museums, Roman Forum",
        "Tourist places in Japan": "Mount Fuji, Tokyo Tower, Kyoto Temples"
    }

    queries = list(data.keys())
    responses = list(data.values())

    dataset = Dataset.from_dict({"queries": queries, "responses": responses})
    print(f"Dataset prepared. Length: {len(dataset)}")
    return dataset

# Step 3: Split dataset
def split_dataset(dataset):
    print("Splitting dataset...")
    split = dataset.train_test_split(test_size=0.2)
    print(f"Train size: {len(split['train'])}, Test size: {len(split['test'])}")
    return split

# Step 4: Tokenization function (Concatenates input-output for CLM)
def preprocess(examples, tokenizer):
    formatted_texts = [f"Question: {q} Answer: {a}" for q, a in zip(examples["queries"], examples["responses"])]
    tokenized = tokenizer(formatted_texts, truncation=True, max_length=512, padding="max_length")

    # Labels should be same as input_ids (for causal LM training)
    tokenized["labels"] = tokenized["input_ids"]
    return tokenized

# Step 5: Fine-tune the model
def fine_tune_model(train_data, eval_data):
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token  # Set padding token to EOS token for GPT2

    model = GPT2LMHeadModel.from_pretrained(model_name).to(device)

    # Preprocess datasets
    print("Preprocessing dataset...")
    train_data = train_data.map(lambda x: preprocess(x, tokenizer), batched=True)
    eval_data = eval_data.map(lambda x: preprocess(x, tokenizer), batched=True)
    print("Preprocessing completed!")

    # Define training arguments
    training_args = TrainingArguments(
        output_dir="./fine_tuned_model",
        evaluation_strategy="epoch",
        save_strategy="epoch",
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        num_train_epochs=3,
        logging_dir="./logs",
        logging_steps=10,
        save_total_limit=2
    )

    # Data collator
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False  # GPT-2 is causal LM, so MLM=False
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_data,
        eval_dataset=eval_data,
        tokenizer=tokenizer,
        data_collator=data_collator
    )

    print("Starting training...")
    trainer.train()

    # Save the fine-tuned model
    model.save_pretrained("./fine_tuned_model")
    tokenizer.save_pretrained("./fine_tuned_model")
    print("Fine-tuned model saved successfully!")

    return model, tokenizer  # ✅ Ensure return is inside function

# Defining generate responses
def generate_response(model, tokenizer, query):
    text_generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)
    response = text_generator(f"Question: {query} Answer:", max_length=100, num_return_sequences=1)

    # Extracting the generated text
    return response[0]["generated_text"].split("Answer:")[-1].strip()

# Prepare dataset
dataset = prepare_dataset()
split_data = split_dataset(dataset)

# Call fine_tune_model to train and get the tokenizer and model
model, tokenizer = fine_tune_model(split_data["train"], split_data["test"])  # The function only returns model and tokenizer

# Create a text generation pipeline using the fine-tuned model and tokenizer
generator = pipeline("text-generation", model="./fine_tuned_model", tokenizer=tokenizer)

def generate_response(query):
    return data.get(query, "I don't have information about that.")

# Get user query
user_query = input("Enter your query: ")

# Generate and print the response
generated_response = generate_response(user_query)
print("Generated Response:", generated_response)
