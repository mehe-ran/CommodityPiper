# CommodityPiper

CommodityPiper is a data pipeline built to extract, clean, and store international commodity pricing data. It handles raw spot prices for bulk materials, normalizes cross-border forex rates to a USD baseline, and loads the structured data into a PostgreSQL database.

The data is served through a FastAPI backend that includes built-in analytics endpoints, making it easy to query time-series data, calculate price spreads, and feed downstream forecasting models.

## Features

* **Asynchronous Extraction:** Uses FastAPI Background Tasks to scrape and ingest market data without blocking the main API thread.
* **Analytics Engine:** Built-in endpoints to calculate cross-border price spreads, 7-day moving averages, and 30-day volatility indexes.
* **Endpoint Security:** Custom dependency injection to require API key authentication for all data-altering and extraction routes.
* **Performance Logging:** HTTP middleware that intercepts requests and logs exact processing times in milliseconds.
* **Containerized Infrastructure:** Fully dockerized with database health checks and CORS middleware for easy frontend integration.

## System Architecture

* **Extraction:** Scrapes raw pricing data from global hubs (South Africa, India, Turkey, China, US, EU, Australia).
* **Transformation:** Cleanses unstructured inputs and normalizes currency fluctuations.
* **Storage:** Saves time-series data in a relational PostgreSQL data warehouse using an optimized star schema.
* **API:** Exposes the data via RESTful endpoints.

## Tech Stack

* **Backend:** Python 3.12, FastAPI
* **Database:** PostgreSQL, SQLAlchemy, Psycopg2
* **Infrastructure:** Docker, Docker Compose
* **Data Processing:** Pandas
* **Testing:** Pytest, HTTPX

## Setup Instructions (Docker)

Running the project via Docker is recommended as it handles the PostgreSQL setup automatically.

```bash
# Clone the repository
git clone [https://github.com/mehe-ran/CommodityPiper.git](https://github.com/mehe-ran/CommodityPiper.git)
cd CommodityPiper

# Build and start the containers
docker-compose up -d --build
```

The Swagger UI documentation will be available at `http://localhost:8000/docs`. 

## Manual Local Setup

To run the pipeline natively on your machine:

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Ensure you have a local PostgreSQL instance running. Create a `.env` file in the root directory and add your connection string:
```text
DATABASE_URL=postgresql://username:password@localhost:5432/commoditypiper
```

Start the server:
```bash
uvicorn src.main:app --reload
```

## How to Test the Pipeline

The data modification and extraction endpoints are locked down. Here is how to authenticate and test the pipeline locally.

### 1. Open the Dashboard
Navigate to `http://localhost:8000/docs` to view the Swagger UI.

![API Dashboard](assets/dashboard.png)

### 2. Generate a Test API Key
Scroll down to the **`POST /auth/generate`** endpoint. Click **"Try it out"**, enter a dummy client name, and hit execute. Copy the `api_key` from the response body.

![Generate Key](assets/auth_generate.png)

### 3. Authenticate
Scroll to the top of the page and click the green **"Authorize"** button.

![Empty Auth](assets/auth_empty.png)

Paste your copied API key into the value box and click Authorize. The padlocks on the secured endpoints will now appear closed.

![Filled Auth](assets/auth_filled.png)

### 4. Run the Extraction Task
Navigate to the **`POST /extract/`** endpoint, click **"Try it out"**, and execute. The API will immediately return an "accepted" status while the python script scrapes and loads the data in the background.

![Successful Extraction](assets/extract_success.png)

### 5. Query the Data
You can now use the public `GET` endpoints to query the daily prices, calculate moving averages, and check market spreads.

## Future Plans

* Integrate Apache Airflow for better task orchestration and failure retries.
* Add Kafka to stream real-time spot price volatility.
* Implement maritime shipping rates into the spread calculations.