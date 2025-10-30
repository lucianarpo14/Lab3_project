import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import kruskal, kstest


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


def normality_test_ks(df, columns):
    """
    Perform Kolmogorov–Smirnov test for normality (recommended for large datasets).
    Prints results and returns a DataFrame with p-values.
    """
    results = []
    print("\n--- Kolmogorov–Smirnov Normality Test ---")
    for col in columns:
        data = df[col].dropna()
        if len(data) < 3:
            continue
        ks_stat, ks_p = kstest(data, 'norm', args=(np.mean(data), np.std(data)))
        results.append({
            'Variable': col,
            'KS_Statistic': ks_stat,
            'KS_p': ks_p,
            'Normal (p>0.05)': 'Yes' if ks_p > 0.05 else 'No'
        })
        print(f"\n{col}:")
        print(f"  Kolmogorov–Smirnov Statistic = {ks_stat:.5f}")
        print(f"  p-value = {ks_p:.5f}")
        if ks_p > 0.05:
            print(" Data follows a normal distribution (p > 0.05)")
        else:
            print(" Data does NOT follow a normal distribution (p ≤ 0.05)")
    return pd.DataFrame(results)


def kruskal_wallis_test(df, value_col, group_col):
    """
    Perform Kruskal–Wallis H-test to compare medians among groups.
    """
    groups = [g[value_col].values for _, g in df.groupby(group_col)]
    stat, p = kruskal(*groups)
    print("\n--- Kruskal–Wallis Test ---")
    print(f"Statistic = {stat:.5f}, p-value = {p:.5f}")
    if p <= 0.05:
        print("At least one group differs significantly (p ≤ 0.05).")
    else:
        print("No significant difference between groups (p > 0.05).")
    return stat, p


def fishers_ratio(df, feature_col, group_col):
    """
    Calculate Fisher’s Ratio (variance between groups / variance within groups)
    to assess feature discriminability across categories.
    """
    overall_mean = df[feature_col].mean()
    groups = df.groupby(group_col)
    
    # Between-class variance
    between_var = sum([
        len(g) * (g[feature_col].mean() - overall_mean)**2 for _, g in groups
    ]) / (len(groups) - 1)
    
    # Within-class variance
    within_var = sum([
        sum((g[feature_col] - g[feature_col].mean())**2) for _, g in groups
    ]) / (len(df) - len(groups))
    
    fisher_ratio = between_var / within_var
    print(f"\n--- Fisher’s Ratio Test ---")
    print(f"Feature: {feature_col}, Grouping: {group_col}")
    print(f"Between variance: {between_var:.5f}")
    print(f"Within variance: {within_var:.5f}")
    print(f"Fisher’s Ratio: {fisher_ratio:.5f}")
    return fisher_ratio