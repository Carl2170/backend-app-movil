def test_listar_asientos(client):
    response = client.get("/journal-entries/")
    assert response.status_code == 200
    assert "data" in response.json

def test_filtrar_por_periodo(client):
    response = client.get("/journal-entries/period/1")
    assert response.status_code == 200
    assert "data" in response.json

def test_filtrar_por_estado(client):
    response = client.get("/journal-entries/status/DRAFT")
    assert response.status_code == 200
    assert "data" in response.json

def test_filtrar_por_rango(client):
    response = client.get("/journal-entries/range?start=2025-01-01&end=2025-01-31")
    assert response.status_code == 200
    assert "data" in response.json

def test_crear_asiento(client):
    payload = {
        "accountingPeriodId": "1",
        "entryDate": "2025-01-15",
        "description": "Ingreso por ventas",
        "details": [
            {
                "accountId": "1",
                "description": "Ingreso",
                "debitAmount": "0.00",
                "creditAmount": "1000.00"
            },
            {
                "accountId": "2",
                "description": "Caja",
                "debitAmount": "1000.00",
                "creditAmount": "0.00"
            }
        ]
    }
    response = client.post("/journal-entries/", json=payload)
    assert response.status_code == 200
    assert "data" in response.json

def test_postear_asiento(client):
    asiento_id = "1"
    response = client.post(f"/journal-entries/{asiento_id}/post")
    assert response.status_code == 200
    assert "data" in response.json

def test_eliminar_asiento(client):
    asiento_id = "1"
    response = client.delete(f"/journal-entries/{asiento_id}")
    assert response.status_code == 200
    assert "data" in response.json