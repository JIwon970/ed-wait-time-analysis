# Synthetic Data Generation (Python)

This folder contains the Python script used to generate the synthetic Emergency Department (ED) dataset for this project.

---

## Purpose
The purpose of this script is to:
- Practice generating realistic synthetic data using Python
- Simulate Emergency Department waiting time data
- Create a dataset that is safe to use for portfolio projects (no real patient data)

---

## What the Script Does
The Python script:
- Generates random Emergency Department records
- Creates the following fields:
  - Date
  - Hospital Name
  - Triage Category
  - Time
  - Waiting Time (minutes)
  - Treatment Time (minutes)
  - Crowding Level
- Exports the generated data as a CSV file

This CSV file is later:
- Cleaned in Excel
- Saved as a database table
- Used for SQL analysis and dashboards

---

## Tools Used
- Python
- Pandas
- Random
- Datetime

---

## Data Disclaimer
- This dataset is **fully synthetic**
- No real hospital or patient data is included
- The data is created **only for learning and portfolio purposes**
