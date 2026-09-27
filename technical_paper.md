\# Water Quality Risk Classification — Technical Summary



\## Abstract

This project develops a binary classification model to predict water

potability from measurable chemical and physical indicators. Using a

foundational machine learning approach, the model investigates which

water characteristics best separate potable from non-potable samples.



\## Problem Definition

Access to safe drinking water is a critical public health concern.

This project evaluates whether lightweight, interpretable machine

learning models can classify water samples into risk categories using

standard water quality measurements, without relying on paid or

proprietary tools.



\## Dataset

The Water Potability dataset (Kaggle, Aditya Kadiwal) contains \~3,300

samples with 9 numeric features: pH, Hardness, Solids, Chloramines,

Sulfate, Conductivity, Organic\_carbon, Trihalomethanes, and Turbidity,

alongside a binary Potability label. The class distribution is

moderately imbalanced: 60.99% not potable, 39.01% potable.



\## Methodology

Three columns (ph, Sulfate, Trihalomethanes) contained missing values,

which were imputed using the median of each column to preserve

distribution shape without introducing bias from outliers. Duplicate

rows were removed. Data was split 80/20 into train and test sets using

stratified sampling to preserve class balance. Features were scaled

using StandardScaler prior to training the Logistic Regression model.



Two foundational classifiers were trained and compared:

\- Logistic Regression

\- Decision Tree Classifier (max depth = 6)



\## Results and Discussion

Logistic Regression achieved 61% accuracy, but this was misleading:

it predicted the majority class (not potable) for 100% of test samples,

achieving 0% recall on the potable class. This indicates the model

found no usable linear decision boundary for this dataset — a common

failure mode when a linear model faces weakly linearly-separable

classes.



The Decision Tree Classifier performed better across the board,

achieving 64% accuracy with a ROC-AUC of 0.608. Its confusion matrix

(\[\[355, 45], \[190, 66]]) shows it correctly identifies most non-potable

samples but still misses a majority of potable ones (recall 0.26 for

class 1). This suggests the tree relies on threshold-based splits that

partially align with the target but cannot fully separate the classes

using these input features alone.



\## Model Justification

The Decision Tree was selected as the final model because it is the

only one of the two that demonstrates any real discriminative ability

between classes, and its non-parametric structure fits the apparent

non-linear relationships in the data better than a linear model.



\## Limitations

\- Overall recall for the potable class remains low, limiting real-world

&#x20; applicability for safety-critical decisions

\- The dataset size (\~3,300 samples) is relatively small for robust

&#x20; generalization

\- Features are chemical measurements without contextual metadata (e.g.

&#x20; source region, testing method), which may limit predictive signal



\## Future Scope

Future iterations could explore ensemble methods (Random Forest,

Gradient Boosting) to better capture non-linear feature interactions,

apply resampling techniques (SMOTE) to address class imbalance more

directly, and perform feature engineering or interaction terms to

improve class separability.



\## Conclusion

This project demonstrates a complete, reproducible ML pipeline — from

data exploration through deployment via a Streamlit application — while

highlighting the importance of comparing multiple models rather than

assuming any single foundational method will perform well on a given

dataset.



\## References

\- Kadiwal, A. Water Potability Dataset. Kaggle.

&#x20; https://www.kaggle.com/datasets/adityakadiwal/water-potability

