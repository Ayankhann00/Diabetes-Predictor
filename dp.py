import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
dataset = pd.read_csv('diabetes.csv')

# Split into features and labels
X = dataset.drop(columns='Outcome', axis=1)
Y = dataset['Outcome']

# Standardize the data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.25, random_state=2, stratify=Y)

# Train SVM model
classifier = SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Evaluate model
train_accuracy = accuracy_score(classifier.predict(X_train), Y_train)
test_accuracy = accuracy_score(classifier.predict(X_test), Y_test)

print("Training Accuracy:", train_accuracy)
print("Test Accuracy:", test_accuracy)

# Save model and scaler
joblib.dump(classifier, 'svm_model.sav')
joblib.dump(scaler, 'scaler.sav')
