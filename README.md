# cohort-retention
Cohort Retention using MongoDB aggregation and FastAPI to track user engagement over time.
Problem

Group users by signup month (cohort) and calculate retention in subsequent months.

 Tech Stack

* MongoDB (Aggregation Pipeline)
* Python (FastAPI)

Approach

1. Convert signup date into cohort (YYYY-MM)
2. Calculate month difference between signup and activity
3. Group users by cohort and month difference
4. Count users and calculate retention

Jan 2024 → 100%, 60%, 40%

1. Import sample_data.json into MongoDB
2. Run cohort_pipeline.js in MongoDB Compass
3. (Optional) Run FastAPI app using:
   uvicorn app:app --reload

## 💡 Insight

Efficient cohort analysis using MongoDB aggregation without heavy backend processing.
