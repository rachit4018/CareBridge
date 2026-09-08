FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /code

RUN apt-get update && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first so the pip layer caches unless deps change.
COPY requirements/ requirements/
RUN pip install --no-cache-dir -r requirements/local.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
