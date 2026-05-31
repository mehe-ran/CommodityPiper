from fastapi.testclient import TestClient
from src.main import app

# initialize the test client
client = TestClient(app)

# test the root health check endpoint
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "pipeline": "commoditypiper active"}