from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    res = client.get('/')
    assert res.status_code == 200
    assert 'Welcome to the FastAPI Time API' in res.json().get('message', '')

def test_current_time():
    res = client.get('/current-time')
    assert res.status_code == 200
    data = res.json()
    assert 'current_time' in data
    # simple format check: ISO-like with 'T' or just presence
    assert isinstance(data['current_time'], str) and len(data['current_time']) > 0
    # mensaje adicional
    assert data.get('message') == 'Que onda perros!'
