# Topic 14 Answers

1. Scheduling decides when a job runs, while orchestration manages the broader workflow and dependencies around that run.
2. Idempotency means a job can run repeatedly without causing incorrect duplicate effects.
3. Retries help recover from temporary issues such as network or service instability.
4. Bad retries can duplicate loads, overload systems, or hide deeper failures.
5. Orders should not load before customers if the order table depends on valid customer keys.
6. A finance report pipeline may need to finish by 7 a.m. every business day.
7. Alerting matters so teams know quickly when a pipeline misses, fails, or degrades.
8. Airflow, Prefect, or Dagster
9. Recurring jobs need logging so support teams can diagnose failures and timing issues.
10. Backfilling may be needed after a source outage or after fixing a failed scheduled run.
11. Modular steps are easier to rerun, test, and troubleshoot.
12. Make it idempotent, log clearly, validate inputs, and separate extraction from loading.
