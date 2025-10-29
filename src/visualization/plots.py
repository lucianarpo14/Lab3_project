import matplotlib.pyplot as plt
import scipy.stats as stats

def plot_histogram_by_group(df, col, group_col):
    """Plot histograms of a numeric variable separated by group."""
    groups = df[group_col].unique()
    for g in groups:
        subset = df[df[group_col] == g][col]
        plt.hist(subset, bins=30, alpha=0.5, label=str(g))
    plt.legend()
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {col} by {group_col}')
    plt.show()