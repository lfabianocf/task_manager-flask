FROM python:3.11-slim

WORKDIR /app

ENV PYTHONPATH=/app
# Aponta diretamente para o arquivo run.py dentro do pacote
ENV FLASK_APP=todo_project/run.py 

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando explícito chamando o arquivo configurado acima
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]