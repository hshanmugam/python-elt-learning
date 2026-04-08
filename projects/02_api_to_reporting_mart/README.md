# Project 2: API to Reporting Mart

## Scenario

A product team exposes customer order events through an API. The analytics team wants an ELT pattern where raw API payloads are loaded first and transformed later into a reporting mart.

## ELT flow

1. Extract simulated API JSON
2. Load raw events into a landing table
3. Transform raw events into a reporting table
4. Query business summaries
