import os
from todo_project import app, db
from flask import Response

from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

# Inicializa o Prometheus desativando o path automático
metrics = PrometheusMetrics(app, path=None)

# Força a criação da rota direto no objeto 'app' principal carregado
@app.route("/metrics")
def prometheus_metrics():
    data = generate_latest()
    return Response(data, mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=os.environ.get("DEBUG", "False") == "True"
    )
    