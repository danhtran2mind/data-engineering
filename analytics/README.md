# Analytics & Visualization

## DuckDB

Run ad-hoc queries:

```bash
duckdb /workspaces/data-engineering/analytics/data.duckdb
-- Example query:
SELECT * FROM taxi_daily LIMIT 10;
```

## LockerStudio

1. Open LockerStudio.
2. Connect to DuckDB file at `/workspaces/data-engineering/analytics/data.duckdb`.
3. Build dashboards using the processed tables.
