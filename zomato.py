 # Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
# Loading Dataset
print("\nLoading the dataset")
df = pd.read_csv("zomato.csv", encoding="latin1")
print(f"Shape of data: {df.shape}")
print(f"This means: {df.shape[0]} rows (restaurants) and {df.shape[1]} columns (features).")
# Show First 10 Rows
print(df.head(10))
# Show Column Names
df.columns
#Show columns name
df.tail(3)
 # Print All Columns with Numbering
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")
    
 