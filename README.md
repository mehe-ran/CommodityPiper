# CommodityPiper

CommodityPiper is an automated, enterprise-grade data engineering pipeline designed to handle the volatile and fragmented data of international commodity trading. It extracts global spot prices for bulk materials, normalizes cross-border forex rates, and loads the cleaned data into a centralized data warehouse.

This structured data is served via a secured RESTful backend equipped with an advanced analytics engine, providing a clean ingestion point for downstream predictive AI models, time-series forecasting algorithms, and arbitrage calculations.

## Enterprise Features

* **Asynchronous Extraction Engine:** Scrapes and ingests raw market data from global pricing hubs using FastAPI Background Tasks to ensure zero API blocking.
* **Advanced Analytics Engine:** Calculates real-time price spreads for cross-border arbitrage, 7-day rolling moving averages, and 30-day standard deviation volatility indexes.
* **Security & Authentication:** All write and extraction endpoints are heavily secured using dependency-injected API Key validation.
* **Performance Monitoring:** Custom HTTP middleware tracks and logs exact millisecond processing times for every request.
* **Robust Infrastructure:** Fully containerized via Docker, protected by CORS middleware, and continuously verified via deep database health checks.

## System Architecture

* **Extraction:** Ingests raw market data focusing on international bulk materials and scrap markets. It tracks volatile trade routes and pricing hubs globally, including South Africa, India, Turkey, China, the United States, the European Union, and Australia.
* **Transformation & Analytics:** Cleanses unstructured inputs, normalizes currency fluctuations to create a unified USD baseline, and calculates live price spreads.
* **Loading:** Stores the normalized time-series data in a relational PostgreSQL data warehouse using a star schema optimized for fast analytical querying.
* **Serving:** Exposes the data lake through a FastAPI backend.

## Technology Stack

* **Backend:** Python 3.x, FastAPI
* **Database:** PostgreSQL, SQLAlchemy, Psycopg2
* **Infrastructure:** Docker, Docker Compose
* **Data Processing:** Pandas
* **Testing:** Pytest, HTTPX

## Getting Started (Docker)

The easiest way to run CommodityPiper is via Docker.

```bash
# clone the repository
git clone [https://github.com/mehe-ran/CommodityPiper.git](https://github.com/mehe-ran/CommodityPiper.git)
cd CommodityPiper

# build and start the pipeline
docker-compose up -d