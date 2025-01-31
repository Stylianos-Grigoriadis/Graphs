import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn as sns
import numpy as np


plt.rcParams.update({
    "font.family": "serif",  # Use serif font
    "font.size": 16})


directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\Education\Classes\Advanced Statistics\Final project'
os.chdir(directory)

Old = pd.read_excel(r'results Isometrics all 2.xlsx', sheet_name='Old all')
Young = pd.read_excel(r'results Isometrics all 2.xlsx', sheet_name='Young all')

print(Old.columns)
print(Young.columns)

Young_SaEn_80 = Young['SaEn_80_Average'].to_numpy()
Young_SaEn_60 = Young['SaEn_60_Average'].to_numpy()
Young_SaEn_40 = Young['SaEn_40_Average'].to_numpy()
Young_SaEn_20 = Young['SaEn_20_Average'].to_numpy()
Young_SaEn_05 = Young['SaEn_05_Average'].to_numpy()

Old_SaEn_80 = Old['SaEn_80_Average'].to_numpy()
Old_SaEn_60 = Old['SaEn_60_Average'].to_numpy()
Old_SaEn_40 = Old['SaEn_40_Average'].to_numpy()
Old_SaEn_20 = Old['SaEn_20_Average'].to_numpy()
Old_SaEn_05 = Old['SaEn_05_Average'].to_numpy()

Young_sd_80 = Young['sd_80_Average'].to_numpy()
Young_sd_60 = Young['sd_60_Average'].to_numpy()
Young_sd_40 = Young['sd_40_Average'].to_numpy()
Young_sd_20 = Young['sd_20_Average'].to_numpy()
Young_sd_05 = Young['sd_05_Average'].to_numpy()

Old_sd_80 = Old['sd_80_Average'].to_numpy()
Old_sd_60 = Old['sd_60_Average'].to_numpy()
Old_sd_40 = Old['sd_40_Average'].to_numpy()
Old_sd_20 = Old['sd_20_Average'].to_numpy()
Old_sd_05 = Old['sd_05_Average'].to_numpy()

mvc_levels = ["5%", "20%", "40%", "60%", "80%"]

# Create a list to store all data
data_list = []

# Append Young data
for i, values in enumerate([Young_sd_05, Young_sd_20, Young_sd_40, Young_sd_60, Young_sd_80]):
    for val in values:
        data_list.append(["Young", mvc_levels[i], val])

# Append Old data
for i, values in enumerate([Old_sd_05, Old_sd_20, Old_sd_40, Old_sd_60, Old_sd_80]):
    for val in values:
        data_list.append(["Old", mvc_levels[i], val])

# Convert to DataFrame
df = pd.DataFrame(data_list, columns=["Group", "MVC %", "SD"])

# Set categorical order to match the required order
df["MVC %"] = pd.Categorical(df["MVC %"], categories=mvc_levels, ordered=True)

# Create the box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x="MVC %", y="SD", hue="Group", data=df, palette="coolwarm", width=0.6, showfliers=False)

# Labels and title
plt.xlabel("MVC Percentage")
plt.ylabel("Standard Deviation")
plt.title("Comparison of Standard Deviation Across MVC Levels")
plt.legend(title="Group")

# Show the plot
plt.show()


mvc_levels = ["5%", "20%", "40%", "60%", "80%"]

# Create a list to store all data
data_list = []

# Append Young data
for i, values in enumerate([Young_SaEn_05, Young_SaEn_20, Young_SaEn_40, Young_SaEn_60, Young_SaEn_80]):
    for val in values:
        data_list.append(["Young", mvc_levels[i], val])

# Append Old data
for i, values in enumerate([Old_SaEn_05, Old_SaEn_20, Old_SaEn_40, Old_SaEn_60, Old_SaEn_80]):
    for val in values:
        data_list.append(["Old", mvc_levels[i], val])

# Convert to DataFrame
df = pd.DataFrame(data_list, columns=["Group", "MVC %", "SaEn"])

# Set categorical order to match the required order
df["MVC %"] = pd.Categorical(df["MVC %"], categories=mvc_levels, ordered=True)

# Create the box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x="MVC %", y="SaEn", hue="Group", data=df, palette="coolwarm", width=0.6, showfliers=False)

# Labels and title
plt.xlabel("MVC Percentage")
plt.ylabel("Sample Entropy")
plt.title("Comparison of Standard Deviation Across MVC Levels")
plt.legend(title="Group")

# Show the plot
plt.show()