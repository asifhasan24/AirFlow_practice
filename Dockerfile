FROM apache/airflow:2.5.0

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER airflow

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
