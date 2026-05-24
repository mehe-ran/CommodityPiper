# CommodityPiper

CommodityPiper is an automated data engineering pipeline designed to handle the volatile and fragmented data of international commodity trading. It extracts global spot prices for bulk materials, normalizes cross-border forex rates, and loads the cleaned data into a centralized data warehouse. 

This structured data is served via a RESTful backend, providing a clean ingestion point for downstream predictive AI models, time-series forecasting algorithms, and financial analytics.

## System Architecture

The pipeline follows a robust Extract, Transform, Load, and Serve pattern designed for scalability and data integrity.

* **Extraction:** Ingests raw market data focusing on international steel and scrap metal markets. It tracks volatile trade routes and pricing hubs globally, including South Africa, India, Turkey, China, the United States, the European Union, and Australia.
* **Transformation:** Cleanses unstructured inputs and normalizes currency fluctuations to create a unified pricing baseline across major global currencies.
* **Loading:** Stores the normalized time-series data in a relational PostgreSQL data warehouse using a star schema optimized for fast analytical querying.
* **Serving:** Exposes the data lake through a FastAPI backend, allowing external AI systems to query the exact historical or real-time spreads needed for prediction models.

## Technology Stack

* **Language:** Python 3.x
* **Framework:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Data Processing:** Pandas, Psycopg2

## Getting Started

Follow these steps to set up the data pipeline locally.

### 1. Clone the Repository

```bash
# clone the repository
git clone [https://github.com/mehe-ran/CommodityPiper.git](https://github.com/mehe-ran/CommodityPiper.git)
cd CommodityPiper
```

### 2. Environment Setup

Create a virtual environment and install the required dependencies.

```bash
# create virtual environment
python -m venv venv

# activate the virtual environment (windows)
venv\Scripts\activate

# activate the virtual environment (mac/linux)
source venv/bin/activate

# install pipeline dependencies
pip install -r requirements.txt
```

### 3. Database Configuration

You will need a running instance of PostgreSQL. Create a `.env` file in the root directory and add your connection string.

```text
# local postgres configuration
DATABASE_URL=postgresql://username:password@localhost:5432/commoditypiper
```

### 4. Running the API

Start the FastAPI server using Uvicorn to verify the connection and serve the endpoints.

```bash
# start the server with hot reloading
uvicorn src.main:app --reload
```

The API documentation will be available at `http://127.0.0.1:8000/docs`.

## Future Roadmap

* Integration of Apache Airflow for robust task orchestration and failure retries.
* Implementation of Kafka for real-time streaming of spot price volatility.
* Advanced mapping for maritime shipping rates and logistics overhead.