"""
Simple data analysis example using pandas
This demonstrates basic Python + uv setup
"""

import pandas as pd
import numpy as np

# Create sample data
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'score': [85, 92, 78, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display data
print("Student Data:")
print(df)
print("\n" + "="*50 + "\n")

# Summary statistics
print("Summary Statistics:")
print(df.describe())
print("\n" + "="*50 + "\n")

# Calculate metrics
avg_score = df['score'].mean()
max_score = df['score'].max()
min_score = df['score'].min()

print(f"Average Score: {avg_score:.2f}")
print(f"Maximum Score: {max_score}")
print(f"Minimum Score: {min_score}")
print("\n" + "="*50 + "\n")

# Find top performer
top_student = df.loc[df['score'].idxmax()]
print(f"Top Performer: {top_student['name']} with score {top_student['score']}")

# Made with Bob
