"""Interactive Streamlit dashboard for the student performance dataset."""

from pathlib import Path

import pandas as pd
import streamlit as st


SCORE_COLUMNS = ["math_score", "reading_score", "writing_score"]
DATA_PATH = Path(__file__).parents[1] / "data" / "student_performance.csv"


@st.cache_data
def load_data(csv_path: str) -> pd.DataFrame:
	"""Load the CSV and add each student's overall average score."""
	data = pd.read_csv(csv_path)
	data["overall_score"] = data[SCORE_COLUMNS].mean(axis=1).round(2)
	return data


st.set_page_config(page_title="Student Performance Analysis", layout="wide")
st.title("Student Performance Analysis")
st.write("Explore study habits, attendance, and subject scores from the student dataset.")

student_data = load_data(str(DATA_PATH))

st.sidebar.header("Filters")
gender_options = ["All"] + sorted(student_data["gender"].dropna().unique().tolist())
selected_gender = st.sidebar.selectbox("Gender", gender_options)

filtered_data = student_data.copy()
if selected_gender != "All":
	filtered_data = filtered_data[filtered_data["gender"] == selected_gender]

if filtered_data.empty:
	st.warning("No students match the selected filter.")
	st.stop()

st.subheader("Key metrics")
metric_columns = st.columns(4)
metric_columns[0].metric("Students", len(filtered_data))
metric_columns[1].metric("Average overall score", f"{filtered_data['overall_score'].mean():.2f}")
metric_columns[2].metric("Average attendance", f"{filtered_data['attendance'].mean():.2f}")
metric_columns[3].metric("Average study hours", f"{filtered_data['study_hours'].mean():.2f}")

st.subheader("Subject-wise average scores")
subject_averages = filtered_data[SCORE_COLUMNS].mean().round(2)
subject_averages.index = [column.replace("_score", "").title() for column in subject_averages.index]
st.bar_chart(subject_averages)

chart_columns = st.columns(2)
with chart_columns[0]:
	st.subheader("Study hours vs overall score")
	st.scatter_chart(filtered_data, x="study_hours", y="overall_score")

with chart_columns[1]:
	st.subheader("Attendance vs overall score")
	st.scatter_chart(filtered_data, x="attendance", y="overall_score")

st.subheader("Key insights")
highest_student = filtered_data.loc[filtered_data["overall_score"].idxmax()]
lowest_student = filtered_data.loc[filtered_data["overall_score"].idxmin()]
study_correlation = filtered_data["study_hours"].corr(filtered_data["overall_score"])
attendance_correlation = filtered_data["attendance"].corr(filtered_data["overall_score"])
strongest_subject = subject_averages.idxmax()

st.write(
	f"- Highest overall score: {highest_student['student_id']} "
	f"({highest_student['overall_score']:.2f})."
)
st.write(
	f"- Lowest overall score: {lowest_student['student_id']} "
	f"({lowest_student['overall_score']:.2f})."
)
st.write(f"- The highest subject average is in {strongest_subject} ({subject_averages.max():.2f}).")
st.write(f"- Study hours and overall score correlation: {study_correlation:.3f}.")
st.write(f"- Attendance and overall score correlation: {attendance_correlation:.3f}.")
st.caption("Correlations describe this dataset and do not prove that one factor causes another.")

st.subheader("Student data")
st.dataframe(filtered_data, use_container_width=True, hide_index=True)