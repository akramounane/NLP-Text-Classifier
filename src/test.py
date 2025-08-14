# test_dataloader.py
from data_loader import load_dataset
dataset_path = "../data/data-augmented.csv"
data = load_dataset(dataset_path, "de")

print(data.head())
