FROM python:3.11.6

WORKDIR /app

COPY requirements.txt .

RUN python3.11 -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3.11", "manage.py", "runserver", "0.0.0.0:8000"]
