"""Basic Day 1 analysis of the student performance CSV file."""

from pathlib import Path

import pandas as pd

def load_data(csv_path: str | Path) -> pd.DataFrame:
    """Load the CSV file into a pandas dataframe."""
    return pd.read_csv(csv_path)


def calculate_basic_averages(data: pd.DataFrame) -> pd.Series:
    """Calculate the average for each subject in the dataset."""
    score_columns = ["math_score", "reading_score", "writing_score"]
    return data[score_columns].mean().round(2)


if __name__ == "__main__":
    csv_path = Path(__file__).parents[1] / "data" / "student_performance.csv"
    student_data = load_data(csv_path)

    # Display basic information before calculating averages.
    print("Dataset information")
    print(f"Rows: {student_data.shape[0]}")
    print(f"Columns: {student_data.shape[1]}")
    print(f"Column names: {list(student_data.columns)}")
    print("\nFirst five records")
    print(student_data.head())
    print("\nBasic subject averages")
    print(calculate_basic_averages(student_data))