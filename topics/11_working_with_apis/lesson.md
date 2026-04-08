# Topic 11: Working with APIs

## Core ideas

APIs allow Python pipelines to request data from applications and services over HTTP.

## Why it matters for ETL and ELT

- Many SaaS systems expose data through REST APIs
- Incremental extraction often depends on API timestamps or pages
- Production jobs must handle timeouts, status codes, and retry behavior

## Key concepts

- HTTP methods such as `GET`
- status codes
- headers and authentication tokens
- JSON parsing
- pagination
- retries and timeouts

## Pipeline examples

- ingest CRM contacts
- pull tickets from a support system
- retrieve daily order events from an application API
