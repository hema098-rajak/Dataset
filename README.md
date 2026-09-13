# Student Performance Analysis

A beginner-friendly five-day Python project for studying fictional student performance data.

This repository is currently at the **Day 1** checkpoint. Only the fictional dataset, basic CSV loading, dataset information, and subject averages are implemented.

## Project structure

```text
Student-Performance-Analysis/
├── data/student_performance.csv
├── src/data_cleaning.py       # Day 2 placeholder
├── src/analysis.py            # Day 1 work
├── dashboard/app.py           # Day 4 placeholder
├── assets/                    # Day 4 screenshot location
├── README.md
├── requirements.txt
└── .gitignore
```

## Setup

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run Day 1 analysis

From the project directory:

```bash
python src/analysis.py
```

The script loads the CSV, displays the number of rows and columns, prints the column names and first five records, and calculates the basic average for each subject.

## Five-day plan

- **Day 1:** Create the fictional dataset and perform basic loading and averages.
- **Day 2:** Add missing-value handling, validation, and preprocessing.
- **Day 3:** Add performance categories, top performers, at-risk students, and insights.
- **Day 4:** Build the interactive dashboard and create its screenshot.
- **Day 5:** Improve documentation, screenshots, and final presentation.

Future-day functionality is intentionally not implemented yet.

## Current setup

```bash
pip install -r requirements.txt
```