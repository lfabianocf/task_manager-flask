FROM python:3.11-slim

WORKDIR /app

#ENV PYTHONPATH=/app
ENV PYTHONPATH=/app:/app/todo_project

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD ["python", "-m", "todo_project.run"]
CMD ["python", "todo_project/run.py"]
