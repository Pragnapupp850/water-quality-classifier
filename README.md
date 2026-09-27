\# Water Quality Risk Classifier



A machine learning capstone project that classifies water samples as potable

or non-potable based on measurable water quality indicators.



\## Problem

Predict whether a water sample is safe to drink (potable) using chemical

and physical properties such as pH, hardness, solids, chloramines, sulfate,

conductivity, organic carbon, trihalomethanes, and turbidity.



\## Dataset

\- \*\*Source\*\*: \[Water Potability Dataset](https://www.kaggle.com/datasets/adityakadiwal/water-potability) by Aditya Kadiwal, Kaggle

\- \*\*Size\*\*: \~3,300 samples, 9 numeric features + binary target (Potability)

\- \*\*Class balance\*\*: 60.99% not potable, 39.01% potable



\## Methodology

1\. Handled missing values (ph, Sulfate, Trihalomethanes) using median imputation

2\. Removed duplicate rows

3\. Split data 80/20 (train/test), stratified by class

4\. Scaled features using StandardScaler (for Logistic Regression)

5\. Trained and compared two foundational models:

&#x20;  - Logistic Regression

&#x20;  - Decision Tree Classifier (max\_depth=6)



\## Model Choice

\*\*Decision Tree Classifier was selected as the final model.\*\*



Logistic Regression collapsed to predicting the majority class only

(100% recall on class 0, 0% recall on class 1), providing no real

predictive value despite 61% accuracy. The Decision Tree captured

non-linear relationships in the data and produced meaningfully better

results across both classes.



\## Results (Decision Tree)

| Metric | Value |

|---|---|

| Accuracy | 64% |

| Precision (Potable) | 0.59 |

| Recall (Potable) | 0.26 |

| ROC-AUC | 0.608 |



Confusion Matrix:

