FROM python:3.11-slim

WORKDIR /app

RUN addgroup --system flaskgroup && adduser --system flaskuser --ingroup flaskgroup

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN mkdir -p /app/data && chown -R flaskuser:flaskgroup /app/data

RUN chown -R flaskuser:flaskgroup /app

USER flaskuser

EXPOSE 5000

CMD ["python", "run.py"]
