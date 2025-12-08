# Emergency Department Wait Time Dashboard (Excel)

## 1. Project Overview
This project analyzes Emergency Department (ED) waiting times using Excel.
The goal is to understand how waiting time changes by hospital, triage category, weekday, and peak hours.
The final result is an interactive Excel dashboard built with Pivot Tables and charts.

---

## 2. Dataset
- Type: Synthetic Emergency Department dataset
- Records: 6,000 rows
- Fields include:
  - Date
  - Hospital Name
  - Triage Category (1–5)
  - Time
  - Waiting Time (minutes)
  - Treatment Time (minutes)
  - ED Crowding Level

*This dataset is synthetic and does not contain real patient data.*

---

## 3. Tools Used
- Microsoft Excel
- Excel Functions for data cleaning
- Pivot Tables
- Slicers
- Excel Charts
- Power Query

---

## 4. Data Cleaning Process (Excel-based)
The data was cleaned using Excel functions:

- Created **Weekday** column from Date
- Extracted **Hour** from Time
- Created **Peak Hour** flag based on busy time rules
- Renamed columns for better readability
- Separated Raw Data and Cleaned Data into different sheets

---

## 5. KPIs Calculated
- Average Wait Time (min)
- Median Wait Time (min)
- Maximum Wait Time (min)
- Total Number of Patients
- Average Peak Hour Wait Time (min)

---

## 6. Dashboard Features
The dashboard allows users to interactively analyze ED wait times by:

- Peak Hour (True / False)
- Hour of the day (0–23)
- Triage Category (1–5)
- Weekday
- Hospital Name

Visualizations include:
- Wait Time by Peak Hours
- Wait Time by Hospital
- Wait Time by Triage Category
- Wait Time by Day of Week
- Wait Time by Hour

---

## 7. Key Insights
- The average ED waiting time is approximately **41 minutes**.
- Peak-hour congestion does **not significantly increase** average waiting time compared to off-peak periods.
- Higher triage levels (4–5) are associated with **much longer waiting times**.

---

## 8. Limitations
- The dataset is synthetic and does not represent real hospital performance.
- Results are for learning and portfolio demonstration purposes only.

---

## 9. Author
Analyst: Jiwon Yang  
Tool: Microsoft Excel  
Project Type: Data Analysis & Dashboard Portfolio
