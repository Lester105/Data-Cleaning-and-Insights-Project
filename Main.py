import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# File path
file_path = 'C:/Users/bradford.bonto/OneDrive - Quantrics/Desktop/Data Cleaning and Insights Project/data/train.csv'

# Check if file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit()

# Load the dataset
df = pd.read_csv(file_path)

# Clean column names: remove any leading/trailing whitespace
df.columns = df.columns.str.strip()

# Drop duplicates and reset index
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

# Show available columns
print("Available columns:", df.columns.tolist())

# 1. Distribution of 'Age'
if 'Age' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'].dropna(), bins=30, kde=True)
    plt.title('Distribution of Age')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("Column 'Age' not found.")

# 2. Correlation Heatmap
plt.figure(figsize=(12, 8))
corr_matrix = df.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# 3. Top Categories - Categorical column
category_column = 'Category'  # Change this if needed

if category_column in df.columns:
    top_categories = df[category_column].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_categories.values, y=top_categories.index, palette='viridis')
    plt.title(f'Top 10 {category_column}')
    plt.xlabel('Count')
    plt.ylabel(category_column)
    plt.show()
else:
    print(f"Column '{category_column}' not found.")

# 4. Boxplot of 'Revenue'
revenue_column = 'Revenue'  # Change this if needed

if revenue_column in df.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[revenue_column].dropna())
    plt.title('Boxplot of Revenue')
    plt.xlabel('Revenue')
    plt.show()
else:
    print(f"Column '{revenue_column}' not found.")
