from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_read_a():
    response = client.get("/math1/5")
    assert response.status_code == 200
    assert response.json()=={"status":"OK","febonacci":[0,1,1,2,3]}


def test_read_b():
    response = client.get("/math2/9")
    assert response.status_code == 200
    assert response.json()=={"status":"OK","factorial":362880} 


def test_read_c():
    response = client.get("/string1/hi")
    assert response.status_code == 200
    assert response.json()=={"status":"OK","length":2}



