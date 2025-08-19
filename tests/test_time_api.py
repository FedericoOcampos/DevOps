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
    text = res.text
    lines = text.splitlines()
    assert lines[0] == 'Que onda perros!'
    assert len(lines) >= 2
    from datetime import datetime as _dt
    _dt.fromisoformat(lines[1])
