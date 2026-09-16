# Student Performance Analysis

A beginner-friendly Python portfolio project that explores how study hours and attendance relate to student subject scores.

## Objectives

- Inspect and clean the student performance data.
- Calculate summary statistics for study habits, attendance, and scores.
- Compare average performance across Math, Reading, and Writing.
- Explore study hours and attendance alongside overall scores.
- Present the results in an interactive Streamlit dashboard.

## Dataset

The project uses `data/student_performance.csv`, which contains 20 student records and these columns:

| Column | Description |
| --- | --- |
| `student_id` | Student identifier |
| `gender` | Student gender recorded in the dataset |
| `study_hours` | Study hours recorded for the student |
| `attendance` | Attendance value recorded for the student |
| `math_score` | Math score |
| `reading_score` | Reading score |
| `writing_score` | Writing score |

## Technologies

- Python
- pandas for loading, cleaning, and analyzing the CSV
- matplotlib for analysis visualizations
- Streamlit for the interactive dashboard

## Project structure

```text
Student-Performance-Analysis/
├── data/
│   └── student_performance.csv
├── dashboard/
│   └── app.py
├── src/
│   ├── analysis.py
│   └── data_cleaning.py
├── assets/
├── README.md
├── requirements.txt
└── .gitignore
```

## Data cleaning

`src/data_cleaning.py` loads the CSV, reports its shape and columns, checks missing values, checks duplicate rows, displays data types, and removes exact duplicate rows in memory. The current CSV has no missing values or duplicate rows, so all 20 records are preserved. No extra cleaned file is created.

Run the cleaning checks from the project root:

```bash
python src/data_cleaning.py
```

## Data analysis

`src/analysis.py` calculates the number of students, average study hours, average attendance, subject averages, and overall average score. It also reports the highest and lowest overall scores and creates matplotlib charts for subject averages, study hours versus overall score, and attendance versus overall score.

The current data produces these averages:

- Average study hours: 3.45
- Average attendance: 82.55
- Average Math score: 71.45
- Average Reading score: 72.65
- Average Writing score: 72.90
- Overall average score: 72.33

The observed correlations in this dataset are 0.981 between study hours and overall score, and 0.984 between attendance and overall score. These values describe association in this dataset; they do not establish causation.

Run the analysis from the project root:

```bash
python src/analysis.py
```

## Key Insights

- The dataset combines study hours, attendance, and Math, Reading, and Writing scores.
- The analysis explores how study habits and attendance relate to overall student scores.
- The project uses Python for data cleaning, summary statistics, visualizations, and the dashboard.

## Dashboard

`dashboard/app.py` provides:

- KPI metrics for student count, average overall score, attendance, and study hours
- Subject-wise average scores
- Study Hours vs Overall Score visualization
- Attendance vs Overall Score visualization
- A gender filter
- Key insights based on the selected data
- A table containing the student records

Start the dashboard from the project root:

```bash
streamlit run dashboard/app.py
```

## Setup

Create a virtual environment and install the project dependencies:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Future improvements

- Add more exploratory charts as the dataset grows.
- Add optional score categories with clearly documented rules.
- Add automated tests for the cleaning and analysis functions.
- Add dashboard controls for score and attendance ranges if they become useful for a larger dataset.