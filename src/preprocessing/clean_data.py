import pandas as pd

def load_raw(path: str) -> pd.DataFrame:
    """Load raw data from an Excel file."""
    return pd.read_excel(path)

def detect_outliers_iqr(series: pd.Series) -> pd.Series:
    """Return boolean series marking outliers using IQR."""
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return (series < lower) | (series > upper)

def preprocess_for_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Filter missing values and mark outliers."""
    df = df.dropna(subset=['pressure'])
    df['is_outlier'] = detect_outliers_iqr(df['pressure'])
    return df