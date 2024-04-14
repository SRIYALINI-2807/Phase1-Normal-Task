import pandas as pd
import matplotlib.pyplot as plt


data = {
    'MONTH': ['January', 'February', 'March', 'April', 'May'],
    'STORECODE': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'QTY': [100, 150, 200, 120, 180],
    'VALUE': [5000, 7500, 10000, 6000, 9000],
    'GRP': ['A', 'B', 'A', 'C', 'B'],
    'SGRP': ['A1', 'B1', 'A1', 'C1', 'B1'],
    'SSGRP': ['A1a', 'B1b', 'A1a', 'C1c', 'B1b'],
    'CMP': ['X', 'Y', 'X', 'Z', 'Y'],
    'MBRD': ['M1', 'M2', 'M1', 'M3', 'M2'],
    'BRD': ['P8', 'P6', 'P8', 'P10', 'P6'],
    'M2': [0.34, 0.34, 0.33, 0.19, 0.15],
    'Label': ['0 - 32.05', '32.05 - 64.10', '64.10 - 96.15', '96.15 - 128.20', '128.20 - 160.25'],
    'Count': [12291, 1092, 425, 192, 108]
}
df = pd.DataFrame(data)


print(df.head())


print("\nDescriptive Statistics:")
print(df.describe())


plt.figure(figsize=(8, 6))
plt.hist(df['QTY'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.title('Distribution of Quantity')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(df['VALUE'], df['QTY'], color='green')
plt.xlabel('Value')
plt.ylabel('Quantity')
plt.title('Value vs Quantity')
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 6))
df['GRP'].value_counts().plot(kind='bar', color='purple')
plt.xlabel('GRP')
plt.ylabel('Count')
plt.title('Counts of GRP Categories')
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 6))
df['MBRD'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'green'])
plt.title('MBRD Distribution')
plt.axis('equal')
plt.show()

