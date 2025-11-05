"""
Lab 3 - Scientific Computing
Author: Luciana Restrepo
Date: 2025-11-04

Main script that integrates preprocessing, analysis, and visualization modules
for the ventilatory pressure dataset.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import 
import pandas as pd
from src.preprocessing.clean_data import load_data, basic_info, preprocess_for_analysis
from src.analysis.exploratory_analysis import (
    descriptive_statistics,
    correlation_analysis,
    detect_outliers_zscore,
    normality_test_ks,
    kruskal_wallis_test,
    fishers_ratio
)
from src.visualization.plots import (
    plot_breath_cycle,
    plot_correlation_heatmap,
    plot_histogram
)

def main():
    # === STEP 1: Load raw datasets ===
    train_path = "data/raw/train.csv"
    test_path = "data/raw/test.csv"
    sample_path = "data/raw/sample_submission.csv"

    train, test, sample = load_data(train_path, test_path, sample_path)

    print("=== Dataset Overview ===")
    basic_info(train)

    # === STEP 2: Data Preprocessing ===
    train_clean = preprocess_for_analysis(train)
    print("\n Preprocessing completed successfully.")

    # === STEP 3: Statistical Analysis ===
    print("\n=== Statistical Analysis ===")
    descriptive_statistics(train_clean)
    correlation_analysis(train_clean)
    detect_outliers_zscore(train_clean, "pressure", threshold=3)

    numeric_cols = ["pressure", "u_in", "u_out"]
    normality_test_ks(train_clean, numeric_cols)

    kruskal_wallis_test(train_clean, value_col="pressure", group_col="R")
    fishers_ratio(train_clean, feature_col="pressure", group_col="R")

    print("\n Statistical analysis completed successfully.")

    # === STEP 4: Data Visualization ===
    print("\n=== Generating Visualizations ===")
    plot_breath_cycle(train_clean, breath_id_col="breath_id", time_col="time_step", pressure_col="pressure")
    plot_correlation_heatmap(train_clean)
    plot_histogram(train_clean, "pressure")

    print("\n Visualization completed successfully.")
    print("\n Lab 3 executed successfully!")

if __name__ == "__main__":
    main()
