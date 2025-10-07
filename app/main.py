from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest
import time
import random

app = Flask(__name__)

# Métriques Prometheus
REQUEST_COUNT = Counter('app_requests_total', 'Total des requêtes', ['endpoint', 'method'])
REQUEST_DURATION = Histogram('app_request_duration_seconds', 'Durée des requêtes')

@app.route('/')
def home():
    REQUEST_COUNT.labels(endpoint='/', method='GET').inc()
    return "Bonjour! L'application fonctionne."

@app.route('/api/data')
@REQUEST_DURATION.time()
def get_data():
    REQUEST_COUNT.labels(endpoint='/api/data', method='GET').inc()
    # Simule un traitement
    time.sleep(random.uniform(0.1, 0.5))
    return {"status": "success", "data": [1, 2, 3]}

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)