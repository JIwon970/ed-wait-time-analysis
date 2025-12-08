# Emergency Department Wait Time Analysis

This project analyzes Emergency Department (ED) waiting times using a complete end-to-end data analytics workflow.

The main objectives of this project were to:
- Measure overall patient waiting time performance
- Identify peak hour patterns
- Compare waiting times by hospital, triage level, weekday, and hour
- Validate Excel KPIs using SQL
- Build interactive dashboards using Power BI
- Summarize findings in a final PDF report

---

## Project Stack

Python → Power Query → Excel → SQL (SQLite) → Power BI → GitHub

- Python: Synthetic data generation  
- Power Query: Data cleaning  
- Excel: EDA, Pivot Tables, KPI Dashboard  
- SQL (SQLite): KPI validation and group-based analysis  
- Power BI: Final interactive dashboard  
- GitHub: Portfolio publishing and version control  

---

## Key KPIs

- Total Patients: 6,000  
- Average Waiting Time: 41.0 minutes  
- Median Waiting Time: 39 minutes  
- Maximum Waiting Time: 119 minutes  
- Average Peak Hour Waiting Time: 39.9 minutes  

All KPI values were first created in Excel and then fully reproduced using SQL.

---

## Project Structure

/excel - Excel dashboard and analysis
/sql - SQL KPI and group analysis queries
/data - SQLite database file
/visuals - SQL result screenshots
/powerbi - Power BI dashboard file (.pbix)
/report - Final PDF analysis report

Each folder contains its own README file for detailed explanations.

---

## SQL Analysis Summary

- All Excel KPIs were fully reproduced using SQL
- Aggregation and filtering were performed using:
  - COUNT, MIN, MAX, AVG
  - GROUP BY
  - CASE WHEN
- Group-based analysis was completed by:
  - Hospital
  - Triage Category
  - Weekday
  - Hour (0–23)
  - Peak vs Non-Peak comparison

SQL results were verified to match the Excel dashboard results.

SQL files location:
/sql/ed_kpi_queries.sql
/sql/ed_group_analysis.sql

---

## Power BI Dashboard Summary

- All KPIs were rebuilt using DAX
- Interactive slicers were applied for:
  - Hospital
  - Triage Category
  - Weekday
  - Hour
  - Peak Hour
- Dynamic visuals replace static Excel charts
- Final dashboard allows real-time filtering and insight exploration

Power BI file location:
/powerbi/ED_Wait_Time_Dashboard.pbix

---

## Final PDF Report

A full project report was created to summarize:

- Data generation process  
- Data cleaning steps  
- Excel dashboard analysis  
- SQL validation results  
- Power BI dashboard insights  

PDF report location:
/report/ED_Wait_Time_Analysis_Report.pdf

---

## Key Skills Demonstrated

- Data cleaning using Power Query  
- KPI development in Excel and SQL  
- SQL aggregation and group-based analysis  
- Peak vs Non-Peak performance analysis  
- DAX-based KPI creation in Power BI  
- End-to-end data analytics workflow  
- GitHub portfolio structuring  

---

## Notes

- This project uses **synthetic data for portfolio purposes**
- No real patient data is included
- This project is for **educational and professional demonstration only**

---

## Author

Analyst: Jiwon Yang  
Project: ED Wait Time Analysis  
Year: 2025
