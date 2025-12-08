-- =========================
-- ED Wait Time KPI Analysis
-- =========================

-- Total Patients
SELECT
  COUNT(*) AS total_patients
FROM ED_dataset_clean;

-- Min / Max / Average Waiting Time
SELECT
  MIN(Waiting_Time_Min) AS min_wait,
  MAX(Waiting_Time_Min) AS max_wait,
  ROUND(AVG(Waiting_Time_Min), 1) AS avg_wait
FROM ED_dataset_clean;

-- Median Waiting Time
SELECT ROUND(AVG(Waiting_Time_Min), 1) AS median_wait
FROM (
  SELECT Waiting_Time_Min
  FROM ED_dataset_clean
  ORDER BY Waiting_Time_Min
  LIMIT 2 - (SELECT COUNT(*) FROM ED_dataset_clean) % 2
  OFFSET (SELECT (COUNT(*) - 1) / 2 FROM ED_dataset_clean)
);

-- Average Peak Hour Waiting Time
SELECT ROUND(AVG(Waiting_Time_Min), 1) AS avg_peak_wait
FROM ED_dataset_clean
WHERE Peak_Hour = 'TRUE';
