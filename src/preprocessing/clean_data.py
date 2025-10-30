import pandas as pd


def load_data(train_path, test_path, sample_path):
    """Load raw CSV files into DataFrames."""
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    sample = pd.read_csv(sample_path)
    return train, test, sample

def basic_info(df):
    """Display basic info, null values, and duplicates."""
    print("\nDataset information:")
    print(df.info())
    print("\nNull values by column:")
    print(df.isnull().sum())
    print("\nDuplicated rows:", df.duplicated().sum())

def preprocess_for_analysis(df):
    """Basic preprocessing: handle nulls, duplicates."""
    df = df.drop_duplicates()
    df = df.fillna(df.mean(numeric_only=True))
    return df
