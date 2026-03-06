import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("dataset/malware_dataset.csv")

print("Dataset Loaded")
print(data.head())
data = data.drop(columns=["hash"])
