import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/titanic.csv") 
print(df.head(10))    # Show first 10 rows of the dataset

print("All modules loaded successfully!")