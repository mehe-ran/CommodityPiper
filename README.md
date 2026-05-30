# CommodityPiper

CommodityPiper is an automated data engineering pipeline designed to handle the volatile and fragmented data of international commodity trading. It extracts global spot prices for bulk materials, normalizes cross-border forex rates, and loads the cleaned data into a centralized data warehouse. 

This structured data is served via a RESTful backend equipped with an analytics engine, providing a clean ingestion point for downstream predictive AI models, time-series forecasting algorithms, and arbitrage calculations.

## System Architecture

* **Extraction Engine:** Scrapes and ingests raw market data from global pricing hubs including South Africa, India, Turkey, China, the United States, the European Union, and Australia.
* **Transformation & Analytics:** Cleanses unstructured inputs, normalizes currency fluctuations, and calculates real-time price spreads for cross-border arbitrage.
* **Loading:** Stores normalized time-series data in a relational PostgreSQL data warehouse using a star schema optimized for fast analytical querying.
* **Serving:** Exposes the data lake through a FastAPI backend.
* **Deployment:** Fully containerized using Docker and Docker Compose.

## Technology Stack

* **Backend:** Python 3.x, FastAPI
* **Database:** PostgreSQL, SQLAlchemy, Psycopg2
* **Infrastructure:** Docker, Docker Compose
* **Data Processing:** Pandas

## Getting Started (Docker)

The easiest way to run CommodityPiper is via Docker.

```bash
# clone the repository
git clone [https://github.com/mehe-ran/CommodityPiper.git](https://github.com/mehe-ran/CommodityPiper.git)
cd CommodityPiper

# build and start the pipeline
docker-compose up -d
```

The API documentation will be instantly available at `http://localhost:8000/docs`.

## Manual Local Setup

If you prefer to run it outside of Docker:

```bash
# create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on windows

# install dependencies
pip install -r requirements.txt
```

Ensure you have a local PostgreSQL instance running and create a `.env` file in the root directory with your connection string:

```text
DATABASE_URL=postgresql://username:password@localhost:5432/commoditypiper
```

```bash
# start the server
uvicorn src.main:app --reload
```

## Future Roadmap

* Integration of Apache Airflow for robust task orchestration and failure retries.
* Implementation of Kafka for real-time streaming of spot price volatility.
* Advanced mapping for maritime shipping rates and logistics overhead.