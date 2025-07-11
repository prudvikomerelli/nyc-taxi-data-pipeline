# NYC Taxi Data Engineering Pipeline 🚕

This is an end-to-end data engineering project that simulates real-time data ingestion and batch processing using open-source tools. It includes ingestion, processing, orchestration, storage, and visualization components.

## 🔧 Stack

- Apache Kafka
- Apache Airflow
- Apache Spark
- PostgreSQL
- MinIO (S3-compatible)
- Apache Superset
- Docker Compose

## 📈 Pipeline Flow

Kafka → MinIO (S3) → Spark → PostgreSQL → Superset

## 🚀 How to Run

```bash
docker-compose up --build
