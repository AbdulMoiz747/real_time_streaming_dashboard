“Table web_logs created in AWS Athena using OpenCSVSerde to read S3 log data (see create_table_web_logs.sql).”

# Real-Time Streaming Analytics Dashboard

This project simulates real-time web traffic and builds a full data pipeline using AWS and Power BI to extract insights from user activity logs.

---

## Project Overview

- Simulate web traffic log data using Python
- Store data in AWS S3 (simulated real-time ingestion)
- Query and analyze the data using AWS Athena (SQL)
- Visualize traffic insights in Power BI dashboards

---

## Tools & Technologies Used

- **Python** – For generating synthetic log data (`generate_logs.py`)
- **AWS S3** – To store raw `.csv` log files
- **AWS Athena** – Serverless SQL queries on S3 data
- **Power BI** – Interactive dashboard for data storytelling
- **SQL** – To query most visited pages, user sessions, and trends

---

## Project Structure

real_time_streaming_dashboard/
├── generate_logs.py # Python script to generate synthetic logs
├── logs.csv # Generated web log data
├── create_table_web_logs.sql # Athena SQL to create table from S3
├── top_pages.csv # Query result: most visited pages 
├── avg_duration.csv # Query result: average session duration 
├── user_activity.csv # Query result: top users by activity 
├── README.md # This file


---

## 📊 Dashboard Overview

The Power BI dashboard includes:

- **Top Visited Pages** – Bar chart of most popular pages
- **Average Session Duration** – Card visual showing user engagement
- **User Activity Overview** – Table of top 10 users by session count
- **Traffic Over Time** *(Optional)* – Trendline of sessions by hour

---

## 🔍 Sample Queries (Athena)

```sql
-- Most visited pages
SELECT page, COUNT(*) AS visits 
FROM web_logs 
GROUP BY page 
ORDER BY visits DESC;

-- Average session duration
SELECT AVG(duration) AS avg_session_duration 
FROM web_logs;

-- Top 10 most active users
SELECT user_id, COUNT(*) AS sessions 
FROM web_logs 
GROUP BY user_id 
ORDER BY sessions DESC 
LIMIT 10;