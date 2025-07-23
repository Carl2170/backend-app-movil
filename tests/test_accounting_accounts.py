def test_listar_cuentas(client):
    response = client.get("/accounting-accounts/")
    assert response.status_code == 200
    assert "data" in response.json

def test_crear_cuenta(client):
    payload = {
        "accountNatureId": "1",
        "chartOfAccountId": "1",
        "code": "101",
        "name": "Caja",
        "level": 1,
        "isActive": True,
        "isTransactional": True
    }
    response = client.post("/accounting-accounts/", json=payload)
    assert response.status_code == 200
    assert "data" in response.json

def test_actualizar_cuenta(client):
    cuenta_id = "1"
    payload = {
        "accountNatureId": "1",
        "chartOfAccountId": "1",
        "code": "101-A",
        "name": "Caja Actualizada",
        "level": 1,
        "isActive": True,
        "isTransactional": True
    }
    response = client.put(f"/accounting-accounts/{cuenta_id}", json=payload)
    assert response.status_code == 200
    assert "data" in response.json

def test_eliminar_cuenta(client):
    cuenta_id = "1"
    response = client.delete(f"/accounting-accounts/{cuenta_id}")
    assert response.status_code == 200
    assert "data" in response.json