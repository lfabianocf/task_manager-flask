FROM python:3.11-slim

WORKDIR /app

# O PYTHONPATH já aponta para /app, garantindo que o módulo 'todo_project' seja visível
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do seu projeto
COPY . .

# Comando direto de execução (evita o CLI do Flask e executa a lógica do banco)
# Ajuste o caminho abaixo caso o seu run.py não esteja na raiz do container
CMD ["python", "todo_project/run.py"]