CREATE EXTERNAL TABLE IF NOT EXISTS web_logs (
  timestamp string,
  user_id int,
  page string,
  duration int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",",
  "skip.header.line.count" = "1"
)
LOCATION 's3://project-logs-abdulmoiz/web_logs/';