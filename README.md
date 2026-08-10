# Diabetes Classification with Gaussian Naive Bayes

🇧🇷 Leia em português: [README.pt-BR.md](README.pt-BR.md)

## Overview

This project applies a **Gaussian Naive Bayes (GaussianNB)** classifier to predict diabetes using two numerical features:

- `glucose_level`
- `blood_pressure`

The dataset was split into training and testing sets using **train_test_split** from scikit-learn.

## Exploratory Data Analysis

- The target variable (`diabetes`) is **well balanced**, verified using `value_counts()` visualized with Plotly (`px.bar`).
- **Glucose level** shows an approximately **normal distribution**.
- **Blood pressure** does not appear to follow a normal distribution and shows **two main concentration regions (bimodal behavior)**.

## Model

- **Algorithm:** Gaussian Naive Bayes (`GaussianNB`)
- **Train/Test Split:** `train_test_split`
- **Evaluation Metric:** **Recall**
- **Additional Evaluation:** **Confusion Matrix**

Recall was chosen because, in a medical classification problem, correctly identifying positive diabetes cases is more important than maximizing overall accuracy.

## Results

The model achieved strong performance:

- **True Negatives:** 86
- **False Positives:** 7
- **False Negatives:** 7
- **True Positives:** 99

These results indicate that the model was effective at identifying diabetic patients while maintaining a good balance between positive and negative predictions.

## Technologies

- Python
- Pandas
- Plotly
- Scikit-learn
- Matplotlib