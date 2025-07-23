def test_listar_planes(client):
    response = client.get("/chart-of-accounts/")
    assert response.status_code == 200
    assert "data" in response.json

def test_crear_plan(client):
    payload = {
        "name": "Plan General",
        "description": "Plan contable base",
        "isDefault": True
    }
    response = client.post("/chart-of-accounts/", json=payload)
    assert response.status_code == 200
    assert response.json["data"]["createChartOfAccount"]["isDefault"] is True