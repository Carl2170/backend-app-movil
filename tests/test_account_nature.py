def test_listar_naturalezas(client):
    response = client.get("/account-natures/")
    assert response.status_code == 200
    assert "data" in response.json

def test_crear_naturaleza(client):
    payload = {
        "name": "Activo",
        "defaultBalanceType": "DEBIT"
    }
    response = client.post("/account-natures/", json=payload)
    assert response.status_code == 200
    assert "data" in response.json
    assert response.json["data"]["createAccountNature"]["name"] == "Activo"