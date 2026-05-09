import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from fastapi.testclient import TestClient
from main import app

# Create one TestClient — reused by all tests
client = TestClient(app)


# ── Root endpoint ──────────────────────────────────────
def test_root_returns_200():
    response = client.get('/')
    assert response.status_code == 200

def test_root_message():
    response = client.get('/')
    assert response.json()['message'] == 'Calculator API is running'


# ── Add endpoint ───────────────────────────────────────
def test_add_two_numbers():
    response = client.get('/add?a=2&b=3')
    assert response.status_code == 200
    assert response.json()['result'] == 5

def test_add_negative_numbers():
    response = client.get('/add?a=-1&b=-1')
    assert response.json()['result'] == -2


# ── Subtract endpoint ──────────────────────────────────
def test_subtract():
    response = client.get('/subtract?a=10&b=4')
    assert response.json()['result'] == 6


# ── Multiply endpoint ──────────────────────────────────
def test_multiply():
    response = client.get('/multiply?a=3&b=4')
def test_multiply():
    response = client.get('/multiply?a=3&b=4')
    assert response.status_code == 200
    assert response.json()['result'] == 12
