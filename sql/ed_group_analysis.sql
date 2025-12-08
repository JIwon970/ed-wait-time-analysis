-- =========================
-- ED Group Analysis Queries
-- =========================

-- By Hospital
SELECT 
  Hospital_Name,
  ROUND(AVG(Waiting_Time_Min), 1) AS avg_wait
FROM ED_dataset_clean
GROUP BY Hospital_Name
ORDER BY avg_wait DESC;

-- By Triage Category
SELECT 
  Triage_Category,
  ROUND(AVG(Waiting_Time_Min), 1) AS avg_wait
FROM ED_dataset_clean
GROUP BY Triage_Category
ORDER BY Triage_Category;

-- By Weekday
SELECT 
  Weekday,
  ROUND(AVG(Waiting_Time_Min), 1) AS avg_wait
FROM ED_dataset_clean
GROUP BY Weekday
ORDER BY avg_wait DESC;

-- By Hour
SELECT 
  Hour,
  ROUND(AVG(Waiting_Time_Min), 1) AS avg_wait
FROM ED_dataset_clean
GROUP BY Hour
ORDER BY Hour;

-- Peak vs Non-Peak Comparison
SELECT
  CASE 
    WHEN Peak_Hour = 'TRUE' THEN 'Peak Hour'
    ELSE 'Non-Peak Hour'
  END AS peak_group,
  ROUND(AVG(Waiting_Time_Min), 1) AS avg_wait
FROM ED_dataset_clean
GROUP BY peak_group;
