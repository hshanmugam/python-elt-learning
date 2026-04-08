# Topic 11 Answers

1. An API is an interface that lets one system request data or actions from another system.
2. `GET`
3. It usually means the request succeeded.
4. It usually means the requested resource was not found.
5. Pagination matters because large datasets are often split across multiple API responses.
6. `headers = {"Authorization": "Bearer <token>"}` 
7. Use `json.loads()` or `response.json()` when using `requests`.
8. `results = payload["results"]`
9. Timeouts stop a pipeline from hanging forever on slow or broken services.
10. Retries should be used carefully so you do not overload an unhealthy API or duplicate processing.
11. Load only records updated after the last successful extraction timestamp.
12. Writing raw JSON first preserves the original source and supports replay or debugging later.
