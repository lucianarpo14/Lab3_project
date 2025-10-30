import pandas as pd
import numpy as np
from scipy import stats

def descriptive_statistics(df):
    """Show basic descriptive statistics."""
    print("\nDescriptive statistics:")
    print(df.describe())

def correlation_analysis(df):
    """Compute and show correlation matrix."""
    corr = df.corr(numeric_only=True)
    print("\nCorrelation matrix:")
    print(corr)
    return corr

def detect_outliers_zscore(df, column, threshold=3):
    """Detect outliers using Z-score."""
    z_scores = np.abs(stats.zscore(df[column]))
    outliers = df[z_scores > threshold]
    print(f"\nOutliers detected in {column}: {len(outliers)}")
    return outliers
