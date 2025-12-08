# SQL Analysis – ED Wait Time Project

This folder contains all SQL queries used for the Emergency Department (ED) Wait Time Analysis project.

All queries were executed using:
- SQLite
- DB Browser for SQLite

The main purpose of this SQL analysis is:
- To reproduce the Excel dashboard KPIs using SQL
- To perform group-based analysis for deeper insights

---

## Files in This Folder

### 1. ed_kpi_queries.sql
This file contains SQL queries for key performance indicators (KPIs):

- Total number of patients
- Minimum waiting time
- Maximum waiting time
- Average waiting time
- Median waiting time
- Average peak hour waiting time

These KPIs were first created in Excel and then fully reproduced using SQL.

---

### 2. ed_group_analysis.sql
This file contains SQL queries for group-based analysis:

- Average waiting time by hospital
- Average waiting time by triage category
- Average waiting time by weekday
- Average waiting time by hour (0–23)
- Peak hour vs non-peak hour comparison

These queries match the charts used in the Excel dashboard.

---

## Database Used

All SQL queries use the following SQLite database file:

