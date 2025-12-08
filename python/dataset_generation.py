import pandas as pd
import numpy as np
import random

# Number of days and number of patient records per day
num_days = 30 
records_per_day = 200 
total_rows = num_days * records_per_day

# Create a continuous 30-day date range
dates = pd.date_range(
    start="2025-01-01", 
    periods=num_days, 
    freq="D")

# Fix hospital names and triage categories
hospitals = ["Royal Melbourne", "St Vincent", "Box Hill", "Mercy", "Western Health"]
triage_levels = [1, 2, 3, 4, 5]

# Create basic colums: Date, Hospital, Triage
data = {
    # Repeat each date 'records_per_day' times so that each day has multiple patient visits
    "Date" : np.repeat(
        dates, 
        records_per_day
        ),

    # Randomly assign a hospital to each patient record
    "Hospital_Name" : np.random.choice(
        hospitals, 
        total_rows
        ),
    
    # Randomly assign triage categories with realistic probability distribution
    # (Higher urgency cases are less common)
    "Triage_Category" : np.random.choice(
        triage_levels, 
        total_rows, 
        p=[0.05, 0.15, 0.40, 0.25, 0.15]
        ),
}

# Generate a random time-of-day value in minutes (0-1440), then convert to HH:MM format
data["Time"] = pd.to_timedelta(np.random.randint(0, 24*60, total_rows), unit="m")

# Generate realistic waiting times based on triage level

# Higher urgency (triage 1-2) should have much shorter waiting times.
# Lower urgency (triage 4-5) tends to wait significantly longer.
waiting_times = []
for triage in data["Triage_Category"]:
    if triage == 1:
        waiting_times.append(np.random.randint(0, 3))
    elif triage == 2:
        waiting_times.append(np.random.randint(5, 15))
    elif triage == 3:
        waiting_times.append(np.random.randint(15, 60))
    elif triage == 4:
        waiting_times.append(np.random.randint(20, 90))
    else:
        waiting_times.append(np.random.randint(30, 120))

data["Waiting_Time_Min"] = waiting_times

# Generate treatment duration (independent random value)

# In real hospitals, treatment time varies widely based on patient condition.
data["Treatment_Time_Min"] = np.random.randint(10, 120, total_rows)

# Classify crowding level based on waiting time

# This creates a simple rule-based indicator for ED congestion.
def crowding(wait):
    if wait<20:
        return "Low"
    elif wait<60:
        return "Medium"
    else:
        return "High"
    
data["ED_Crowding_Level"] = [crowding(w) for w in data["Waiting_Time_Min"]]

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Save dataset to CSV file
df.to_csv("ed_dataset.csv", index=False)

# Display first few rows
df.head()