def test_listar_periodos(client):
    response = client.get("/accounting-periods/")
    assert response.status_code == 200
    assert "data" in response.json

def test_filtrar_por_estado(client):
    response = client.get("/accounting-periods/status/OPEN")
    assert response.status_code == 200
    assert "data" in response.json

def test_crear_periodo(client):
    payload = {
        "name": "2025-Q1",
        "startDate": "2025-01-01",
        "endDate": "2025-03-31",
        "status": "OPEN"
    }
    response = client.post("/accounting-periods/", json=payload)
    assert response.status_code == 200
    assert "data" in response.json

def test_actualizar_periodo(client):
    periodo_id = "1"
    payload = {
        "name": "2025-Q1 Actualizado",
        "startDate": "2025-01-01",
        "endDate": "2025-03-31",
        "status": "CLOSED"
    }
    response = client.put(f"/accounting-periods/{periodo_id}", json=payload)
    assert response.status_code == 200
    assert "data" in response.json

def test_eliminar_periodo(client):
    periodo_id = "1"
    response = client.delete(f"/accounting-periods/{periodo_id}")
    assert response.status_code == 200
    assert "data" in response.json