import requests

# ---------------------------------------------------------------------------
# Simple demo: making GET requests to a public JSON API and inspecting results
# ---------------------------------------------------------------------------

# A test endpoint that returns a single “post” resource in JSON.
endpoint = "https://jsonplaceholder.typicode.com/posts/1"

# 1) Plain GET request (no payload)
response = requests.get(endpoint)

# Raw text body as returned by the server (a JSON‑encoded string).
print("Raw response text:")
print(response.text)

# Parse the JSON into a Python dict for easier access.
print("\nParsed JSON object:")
print(response.json())

# HTTP status code—200 means the request succeeded.
print("\nStatus code:", response.status_code)

# 2) Second GET request, this time passing a dummy JSON payload.
# (This particular API ignores payloads on GET, but it’s useful for illustration.)
response_with_payload = requests.get(endpoint, json={"query": "Hello World"})

print("\nResponse with dummy payload (should look identical):")
print(response_with_payload.text)

print("\nParsed JSON again:")
print(response_with_payload.json())

print("\nStatus code again:", response_with_payload.status_code)
