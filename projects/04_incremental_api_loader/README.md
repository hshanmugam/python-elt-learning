# Project 4: Incremental API Loader

## Scenario

A customer support platform exposes ticket updates through an API. The data team wants a repeatable job that loads only records updated since the last successful run.

## Skills practiced

- API extraction thinking
- incremental loading
- JSON persistence
- scheduling-friendly state management

## Flow

1. Read the last successful watermark
2. Extract only new or changed records
3. Persist the raw payload
4. Update the watermark
