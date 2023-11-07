# -*- coding: utf-8 -*-
"""sprintrelease1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1adIg5vWa2EsbgEO0_2q0_LUAKNw2JA2p

# **Importing Dataset**
"""

import pandas as pd

df = pd.read_csv('/content/Heart_disease_cleveland_new.csv')

new_df = df.dropna()

print(new_df.to_string())

"""# **Data Preprocessing**"""

# Check for missing values
print(df.isnull().sum())

# To impute missing values with the mean
df.fillna(df.mean(), inplace=True)

import matplotlib.pyplot as plt
import seaborn as sns
# Create box plots for numerical features
plt.figure(figsize=(12, 6))
sns.boxplot(data=df.select_dtypes(include=['float64']), orient="h")
plt.title("Box Plots for Numerical Features")
plt.xlabel("Value")
plt.show()

import numpy as np
from scipy import stats

z_scores = np.abs(stats.zscore(df.select_dtypes(include=['float64'])))
outlier_threshold = 3  # You can adjust this threshold as needed
outliers = (z_scores > outlier_threshold).any(axis=1)

# Remove outliers
df_no_outliers = df[~outliers]

# Handle missing values if necessary (e.g., remove rows with missing values)
df_no_outliers.dropna(inplace=True)

# Save the cleaned data to a new CSV file
df_no_outliers.to_csv("cleveland_heart_disease_no_outliers.csv", index=False)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Cleveland Heart Disease dataset
data = pd.read_csv("/content/cleveland_heart_disease_no_outliers.csv")

# Create box plots for numerical features
plt.figure(figsize=(12, 6))
sns.boxplot(data=data.select_dtypes(include=['float64']), orient="h")
plt.title("Box Plots for Numerical Features")
plt.xlabel("Value")
plt.show()

"""# **Balancing Data**"""

import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Load the dataset into a Pandas DataFrame


# Assuming 'target_variable' is the column name for the target variable
X = df.drop('target', axis=1)  # Features
y = df['target']  # Target variable

# Handle categorical variables using one-hot encoding
X = pd.get_dummies(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate the SMOTE object
smote = SMOTE(random_state=42)

# Fit and transform the training data
X_train_oversampled, y_train_oversampled = smote.fit_resample(X_train, y_train)

# Assuming 'target_variable' is the column name for the target variable
# Before oversampling
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Before Oversampling')
plt.hist(y_train, bins=len(y_train.unique()), alpha=0.7, color='b', label='Original',edgecolor='black')
plt.xlabel('Target Variable')
plt.ylabel('Count')
plt.legend()

import matplotlib.pyplot as plt

# Count the occurrences of each class before oversampling
class_counts_before = y.value_counts()

# Count the occurrences of each class after oversampling
y_train_oversampled_counts = pd.Series(y_train_oversampled).value_counts()

# Plotting the bar graph
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
class_counts_before.plot(kind='bar', color='blue')
plt.title('Class Distribution (Before Oversampling)')
plt.xlabel('Class')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
y_train_oversampled_counts.plot(kind='bar', color='green')
plt.title('Class Distribution (After Oversampling)')
plt.xlabel('Class')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

"""# **Data Visualization**"""

fig,ax=plt.subplots(ncols=7,nrows=2,figsize=(20,20))
hg=df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target']]
index=0
ax=ax.flatten()
for col,value in hg.items():
  sns.boxplot(y=col,data=hg,ax=ax[index])
  index +=1
plt.tight_layout(pad=0.5,w_pad=0.7,h_pad=5.0)

import seaborn as sns
sns.pairplot(df, hue='target', diag_kind='kde')
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Assuming 'target' is the name of the column containing the target variable (0 or 1 for heart disease)
X = data.drop('target', axis=1)  # Features (all columns except the target)
y = data['target']  # Target variable

# Split the dataset into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Random Forest classifier
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the Random Forest model
random_forest.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = random_forest.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)