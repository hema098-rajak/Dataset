"""Simple data-quality checks and cleaning for the student performance data."""

from pathlib import Path

import pandas as pd


def load_data(csv_path: str | Path) -> pd.DataFrame:
	"""Load the student performance CSV into a pandas DataFrame."""
	return pd.read_csv(csv_path)


def inspect_data(data: pd.DataFrame) -> None:
	"""Print basic information that helps us understand the dataset."""
	print("Dataset information")
	print(f"Shape: {data.shape}")
	print(f"Column names: {list(data.columns)}")
	print("\nMissing values by column")
	print(data.isna().sum())
	print(f"\nDuplicate rows: {data.duplicated().sum()}")
	print("\nData types")
	print(data.dtypes)


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
	"""Return the data with exact duplicate rows removed."""
	cleaned_data = data.drop_duplicates().copy()
	removed_rows = len(data) - len(cleaned_data)
	print(f"\nRemoved duplicate rows: {removed_rows}")
	return cleaned_data


if __name__ == "__main__":
	csv_path = Path(__file__).parents[1] / "data" / "student_performance.csv"
	student_data = load_data(csv_path)

	# Inspect the original data before applying the minimal cleaning step.
	inspect_data(student_data)
	cleaned_student_data = clean_data(student_data)
	print(f"Cleaned shape: {cleaned_student_data.shape}")