 #import necessary libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# load csv file
df = pd.read_csv(r"C:\Users\ADMIN\Downloads\all_combined.csv")

#Clean the numeric columns
df['foreign_gross'] = pd.to_numeric(df['foreign_gross'].replace(r'[\$,]', '', regex=True), errors='coerce')
df['domestic_gross_y'] = pd.to_numeric(df['domestic_gross_y'].replace(r'[\$,]', '', regex=True), errors='coerce')

# Define groups based on rating
high_rating = df[df['vote_average'] > 7]
low_rating = df[df['vote_average'] <= 7]

# Drop missing values for revenue
high_revenue = high_rating['worldwide_gross'].dropna()
low_revenue = low_rating['worldwide_gross'].dropna()

# Run t-test
t_stat, p_value = ttest_ind(high_revenue, low_revenue, equal_var=False)

# Print results
print("=== Hypothesis Test: High vs Low Rated Movies ===")
print(f"Mean Revenue (High Rating > 7): ${high_revenue.mean():,.2f}")
print(f"Mean Revenue (Low Rating ≤ 7): ${low_revenue.mean():,.2f}")
print(f"T-statistic: {t_stat:.2f}")
print(f"P-value: {p_value:.5f}")

#Plot the comparison
plt.figure(figsize=(8, 5))
plt.bar(['High Rated', 'Low Rated'], [high_revenue.mean(), low_revenue.mean()], color=['green', 'red'])
plt.title('Average Revenue: High vs Low Rated Movies')
plt.ylabel('Revenue ($)')
plt.tight_layout()
plt.show()