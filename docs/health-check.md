# Health check endpoint

The application exposes a technical health endpoint:

```text
http://localhost:8000/health/
```

It returns a small JSON response:

```json
{
  "status": "ok",
  "service": "restaurant-menu"
}
```

Docker uses this endpoint to check that the container is running and that Django can respond to HTTP requests.
