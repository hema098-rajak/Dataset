"""Beginner-friendly analysis of the student performance CSV file."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


SCORE_COLUMNS = ["math_score", "reading_score", "writing_score"]


def load_data(csv_path: str | Path) -> pd.DataFrame:
    """Load the CSV file into a pandas DataFrame."""
    return pd.read_csv(csv_path)


def add_overall_score(data: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of the data with each student's overall score."""
    analyzed_data = data.copy()
    analyzed_data["overall_score"] = analyzed_data[SCORE_COLUMNS].mean(axis=1)
    return analyzed_data


def add_performance_category(data: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of the data with each student's performance category."""
    analyzed_data = add_overall_score(data)
    category_bins = [float("-inf"), 50, 70, 85, float("inf")]
    category_labels = ["Needs Improvement", "Average", "Good", "Excellent"]
    analyzed_data["performance_category"] = pd.cut(
        analyzed_data["overall_score"], bins=category_bins, labels=category_labels
    )
    return analyzed_data


def calculate_statistics(data: pd.DataFrame) -> dict[str, float]:
    """Calculate the main summary statistics for the dataset."""
    analyzed_data = add_overall_score(data)
    return {
        "number_of_students": int(len(analyzed_data)),
        "average_study_hours": round(analyzed_data["study_hours"].mean(), 2),
        "average_attendance": round(analyzed_data["attendance"].mean(), 2),
        "average_math_score": round(analyzed_data["math_score"].mean(), 2),
        "average_reading_score": round(analyzed_data["reading_score"].mean(), 2),
        "average_writing_score": round(analyzed_data["writing_score"].mean(), 2),
        "overall_average_score": round(analyzed_data["overall_score"].mean(), 2),
        "median_overall_score": round(analyzed_data["overall_score"].median(), 2),
    }


def create_visualizations(data: pd.DataFrame) -> plt.Figure:
    """Create simple charts for subject averages and two score relationships."""
    analyzed_data = add_overall_score(data)
    subject_averages = analyzed_data[SCORE_COLUMNS].mean()

    figure, axes = plt.subplots(1, 3, figsize=(15, 4))

    subject_averages.plot(kind="bar", ax=axes[0], color="#2f6690")
    axes[0].set_title("Average Score by Subject")
    axes[0].set_ylabel("Average score")
    axes[0].set_ylim(0, 100)
    axes[0].tick_params(axis="x", rotation=0)

    axes[1].scatter(analyzed_data["study_hours"], analyzed_data["overall_score"], color="#3a7d44")
    axes[1].set_title("Study Hours vs Overall Score")
    axes[1].set_xlabel("Study hours")
    axes[1].set_ylabel("Overall score")

    axes[2].scatter(analyzed_data["attendance"], analyzed_data["overall_score"], color="#c75146")
    axes[2].set_title("Attendance vs Overall Score")
    axes[2].set_xlabel("Attendance")
    axes[2].set_ylabel("Overall score")

    figure.tight_layout()
    return figure


def print_analysis(data: pd.DataFrame) -> None:
    """Print summary statistics and simple observations from the data."""
    analyzed_data = add_performance_category(data)
    statistics = calculate_statistics(analyzed_data)

    print("Student performance analysis")
    for name, value in statistics.items():
        label = name.replace("_", " ").title()
        print(f"{label}: {value}")

    print("\nPerformance category counts:")
    category_counts = analyzed_data["performance_category"].value_counts().reindex(
        ["Needs Improvement", "Average", "Good", "Excellent"], fill_value=0
    )
    for category, count in category_counts.items():
        print(f"{category}: {count}")

    highest_student = analyzed_data.loc[analyzed_data["overall_score"].idxmax()]
    lowest_student = analyzed_data.loc[analyzed_data["overall_score"].idxmin()]
    study_correlation = analyzed_data["study_hours"].corr(analyzed_data["overall_score"])
    attendance_correlation = analyzed_data["attendance"].corr(analyzed_data["overall_score"])

    print(f"\nHighest overall score: {highest_student['student_id']} ({highest_student['overall_score']:.2f})")
    print(f"Lowest overall score: {lowest_student['student_id']} ({lowest_student['overall_score']:.2f})")
    print(f"Study hours and overall score correlation: {study_correlation:.3f}")
    print(f"Attendance and overall score correlation: {attendance_correlation:.3f}")


if __name__ == "__main__":
    csv_path = Path(__file__).parents[1] / "data" / "student_performance.csv"
    student_data = load_data(csv_path)

    print_analysis(student_data)
    create_visualizations(student_data)
    plt.show()