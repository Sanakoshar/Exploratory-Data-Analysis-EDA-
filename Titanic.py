# Titanic Dataset EDA

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Dataset
print("Loading Titanic Dataset...\n")

df = pd.read_csv("titanic.csv")  # CSV file same folder me honi chahiye

# First 5 Rows
print("First 5 Rows:")
print(df.head())

# Age Statistics
print("\nAge Statistics:")
print(df['Age'].describe())

# Gender Count
print("\nGender Count:")
print(df['Sex'].value_counts())

# Age Distribution
plt.figure(figsize=(8, 5))
plt.hist(df['Age'].dropna(), bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Fare Boxplot
plt.figure(figsize=(6, 4))
plt.boxplot(df['Fare'].dropna())
plt.title("Fare Boxplot")
plt.show()
df['Sex'].value_counts().plot(kind='bar')
plt.title("Gender Counts")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.show()
df['Survived'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)
plt.title("Survival Percentage")
plt.ylabel("")
plt.show()

# Average Age by Gender
print("\nAverage Age by Gender:")
print(df.groupby('Sex')['Age'].mean())

# Survival Count by Gender
print("\nSurvival Count by Gender:")
print(df.groupby('Sex')['Survived'].value_counts())

# Age vs Fare Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(df['Age'], df['Fare'])
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

# Average Age by Passenger Class
df.groupby('Pclass')['Age'].mean().plot(kind='bar')
plt.title("Average Age by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Age")
plt.show()

# Average Fare by Gender and Class
print("\nAverage Fare by Gender and Passenger Class:")
print(df.groupby(['Sex', 'Pclass'])['Fare'].mean())

# Gender vs Survival
pd.crosstab(df['Sex'], df['Survived']).plot(
    kind='bar',
    stacked=True
)
plt.title("Gender vs Survival")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

print("\nEDA Completed Successfully!")