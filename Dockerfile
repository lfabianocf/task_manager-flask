FROM python:3.11-slim

WORKDIR /app

# Criar usuário não-root
RUN addgroup --system flaskgroup && adduser --system flaskuser --ingroup flaskgroup

# Instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar projeto
COPY . .

# Criar diretório do banco
RUN mkdir -p /app/data && chown -R flaskuser:flaskgroup /app

# Trocar usuário
USER flaskuser

EXPOSE 5000

CMD ["python", "todo_project/run.py"]
