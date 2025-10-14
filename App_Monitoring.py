from flask import Flask
import random, time
from prometheus_client import Counter, Histogram, generate_latest
from waitress import serve   #import here, not inside a function

app = Flask(__name__)

# Metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency')

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    with REQUEST_LATENCY.time():
        time.sleep(random.uniform(0.1, 0.5))  # simulate work
    return "Hello, Prometheus & Grafana"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

# Production server with Waitress
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
