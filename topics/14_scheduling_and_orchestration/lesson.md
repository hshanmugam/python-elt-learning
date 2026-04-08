# Topic 14: Scheduling and Orchestration

## Core ideas

Scheduling decides when a job runs. Orchestration manages dependencies, retries, alerts, and the order of pipeline tasks.

## Why it matters for ETL and ELT

- data must arrive on time for reports and downstream systems
- one task may depend on another finishing successfully
- failed runs often need retries and clear visibility

## Key concepts

- schedules and intervals
- dependencies
- retries
- idempotency
- SLAs
- orchestration platforms such as Airflow, Prefect, or Dagster

## Pipeline examples

- run a daily sales load at 6 a.m.
- load customers before orders
- retry an API extraction if a transient error occurs
