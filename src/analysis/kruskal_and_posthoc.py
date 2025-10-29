# kruskal_and_posthoc.py - Kruskal–Wallis and Dunn post-hoc tests
import pandas as pd
from scipy.stats import kruskal
import scikit_posthocs as sp

def run_kruskal(df, value_col, group_col):
    """Perform Kruskal–Wallis test on independent groups."""
    groups = [g[value_col].values for _, g in df.groupby(group_col)]
    stat, p = kruskal(*groups)
    return stat, p

def dunn_posthoc(df, value_col, group_col, p_adjust='bonferroni'):
    """Perform Dunn post-hoc test with Bonferroni correction."""
    res = sp.posthoc_dunn(df, val_col=value_col, group_col=group_col, p_adjust=p_adjust)
    return res