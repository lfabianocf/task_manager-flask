FROM python:3.11-slim

WORKDIR /app

RUN addgroup --system flaskgroup && adduser --system flaskuser --ingroup flaskgroup

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/data \
    && chown -R flaskuser:flaskgroup /app \
    && chmod -R 777 /app/data

USER flaskuser

EXPOSE 5000

CMD ["python", "-m", "todo_project.run"]
