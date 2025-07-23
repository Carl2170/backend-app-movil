def test_listar_detalles(client):
    response = client.get("/journal-details/")
    assert response.status_code == 200
    assert "data" in response.json

def test_detalle_por_id(client):
    detalle_id = "1"  # reemplazá con un ID válido en tu entorno
    response = client.get(f"/journal-details/{detalle_id}")
    assert response.status_code == 200
    assert "data" in response.json

def test_detalles_por_asiento(client):
    entry_id = "1"  # ID de asiento contable
    response = client.get(f"/journal-details/entry/{entry_id}")
    assert response.status_code == 200
    assert "data" in response.json

def test_detalles_por_cuenta(client):
    account_id = "1"  # ID de cuenta contable
    response = client.get(f"/journal-details/account/{account_id}")
    assert response.status_code == 200
    assert "data" in response.json

def test_balance_por_cuenta(client):
    account_id = "1"
    response = client.get(f"/journal-details/account/{account_id}/balance")
    assert response.status_code == 200
    assert "data" in response.json
    assert "balance" in response.json["data"]["accountBalance"]

def test_crear_detalle(client):
    payload = {
        "accountId": "1",
        "journalEntryId": "1",
        "description": "Movimiento test",
        "debitAmount": "100.00",
        "creditAmount": "0.00"
    }
    response = client.post("/journal-details/", json=payload)
    assert response.status_code == 200
    assert "data" in response.json

def test_actualizar_detalle(client):
    detalle_id = "1"
    payload = {
        "accountId": "1",
        "journalEntryId": "1",
        "description": "Actualizado",
        "debitAmount": "50.00",
        "creditAmount": "0.00"
    }
    response = client.put(f"/journal-details/{detalle_id}", json=payload)
    assert response.status_code == 200
    assert "data" in response.json

def test_eliminar_detalle(client):
    detalle_id = "1"
    response = client.delete(f"/journal-details/{detalle_id}")
    assert response.status_code == 200
    assert "data" in response.json