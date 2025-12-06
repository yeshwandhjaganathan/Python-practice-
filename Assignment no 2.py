# taxis_analysis.py
# -*- coding: utf-8 -*-
"""
Taxis dataset: load, inspect, handle missing values, and visualize.
Author: Yarvy (for Yashwant)
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ---------- 1) Load dataset ----------
print("\n1) Loading 'taxis' dataset (from seaborn)...")
try:
    taxis_df = sns.load_dataset('taxis')
except Exception as e:
    raise RuntimeError("Cannot load 'taxis' dataset. Make sure you have internet or seaborn datasets available.") from e

print(f"Dataset loaded. Shape: {taxis_df.shape}")
print("\nFirst 5 rows:")
print(taxis_df.head())

# Save a quick CSV copy (optional)
out_dir = "taxis_output"
os.makedirs(out_dir, exist_ok=True)
taxis_df.head().to_csv(os.path.join(out_dir, "taxis_head_sample.csv"), index=False)

# ---------- 2) Basic info & missing values ----------
print("\n2) Info and missing-values summary:")
print(taxis_df.info())
print("\nMissing values per column:")
print(taxis_df.isnull().sum())

# Show percent missing
missing_percent = 100 * taxis_df.isnull().sum() / len(taxis_df)
print("\nMissing values (%) per column:")
print(missing_percent.round(2))

# ---------- 3) Simple strategies to handle missing values ----------
df = taxis_df.copy()

# Strategy A: Drop rows with any missing values (demonstration)
df_dropna = df.dropna()
print(f"\nAfter df.dropna(): shape = {df_dropna.shape}  (dropped {len(df)-len(df_dropna)} rows)")

# Strategy B: Fill numeric cols with mean, categorical with mode
num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()

df_fill = df.copy()

# numeric fill with mean
for c in num_cols:
    if df_fill[c].isnull().any():
        mean_val = df_fill[c].mean()
        df_fill[c].fillna(mean_val, inplace=True)

# categorical fill with mode (if exists)
for c in cat_cols:
    if df_fill[c].isnull().any():
        mode_vals = df_fill[c].mode()
        if len(mode_vals) > 0:
            df_fill[c].fillna(mode_vals[0], inplace=True)
        else:
            df_fill[c].fillna('Unknown', inplace=True)

print(f"\nAfter numeric-mean & categorical-mode fill: missing counts =\n{df_fill.isnull().sum()}")

# Strategy C: forward-fill then backward-fill (time-series friendly)
df_ffill = df.copy().fillna(method='ffill').fillna(method='bfill')
print(f"\nAfter ffill/bfill: missing counts =\n{df_ffill.isnull().sum()}")

# Save the cleaned sample
df_fill.head().to_csv(os.path.join(out_dir, "taxis_filled_sample.csv"), index=False)

# ---------- 4) Quick summary statistics ----------
print("\n4) Summary statistics (numeric):")
print(df.describe())

# ---------- 5) Visualizations ----------
print("\n5) Creating visualizations (saved under ./taxis_output/*.png)...")

# Helper: get numeric and categorical columns again
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()

# 5.1 Histogram for each numeric column (limited to first 6 to avoid too many plots)
for i, col in enumerate(numeric_cols[:6], start=1):
    plt.figure(figsize=(6,4))
    df[col].dropna().plot.hist(bins=30)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    fname = os.path.join(out_dir, f"hist_{col}.png")
    plt.savefig(fname)
    plt.close()

# 5.2 Boxplot for numeric columns (combined)
if numeric_cols:
    plt.figure(figsize=(8,6))
    df[numeric_cols[:6]].plot.box()
    plt.title('Boxplot of numeric columns (first up to 6)')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "boxplot_numeric.png"))
    plt.close()

# 5.3 Scatter plot between two numeric columns (choose best available)
if len(numeric_cols) >= 2:
    x_col = numeric_cols[0]
    y_col = numeric_cols[1]
    plt.figure(figsize=(6,5))
    df.plot.scatter(x=x_col, y=y_col)
    plt.title(f'Scatter: {x_col} vs {y_col}')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, f"scatter_{x_col}_vs_{y_col}.png"))
    plt.close()

# 5.4 Bar plot: frequency of first categorical column (if any)
if categorical_cols:
    cat = categorical_cols[0]
    counts = df[cat].value_counts().nlargest(20)  # top 20 categories
    plt.figure(figsize=(8,5))
    counts.plot.bar()
    plt.title(f'Top counts for {cat}')
    plt.xlabel(cat)
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, f"bar_{cat}.png"))
    plt.close()

# 5.5 Time-series line plot if there's a datetime column (pick first)
datetime_cols = df.select_dtypes(include=['datetime', 'datetimetz']).columns.tolist()
if datetime_cols:
    dt = datetime_cols[0]
    # resample counts per day (example)
    temp = df.set_index(dt).resample('D').size()
    plt.figure(figsize=(10,4))
    temp.plot.line()
    plt.title(f'Counts per day (by {dt})')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, f"line_counts_by_{dt}.png"))
    plt.close()
else:
    print("No datetime column detected for time-series plot.")

print("All plots saved. Check the 'taxis_output' directory.")

# ---------- 6) Example EDA answers ----------
print("\n6) Example EDA quick answers:")
print(f"- Number of rows: {len(df)}")
print(f"- Numeric columns found: {numeric_cols}")
print(f"- Categorical columns found: {categorical_cols}")

# If you want, export a final cleaned CSV (filled with mean/mode)
clean_csv_path = os.path.join(out_dir, "taxis_cleaned_fill_mean_mode.csv")
df_fill.to_csv(clean_csv_path, index=False)
print(f"\nCleaned dataset (mean/mode) saved to: {clean_csv_path}")

print("\nScript finished successfully.")
