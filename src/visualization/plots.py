import matplotlib.pyplot as plt
import seaborn as sns

def plot_breath_cycle(df, breath_id_col, time_col, pressure_col):
    """Plot pressure vs time for a given breath cycle."""
    breath_id = df[breath_id_col].iloc[0]
    cycle = df[df[breath_id_col] == breath_id]
    plt.figure(figsize=(8,4))
    plt.plot(cycle[time_col], cycle[pressure_col], label="Airway Pressure")
    plt.xlabel("Time step")
    plt.ylabel("Pressure (cmH2O)")
    plt.title(f"Breath ID {breath_id}")
    plt.legend()
    plt.show()

def plot_correlation_heatmap(df):
    """Plot correlation heatmap for numeric variables."""
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

def plot_histogram(df, column):
    """Plot histogram of a variable."""
    plt.figure(figsize=(8,4))
    sns.histplot(df[column], kde=True, bins=30)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()
