def test_classify_document():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    payload = {
        "filenames": ["w2_2023.pdf", "bank_jan.csv", "paystub.pdf"]
    }
    expected = {
        "results": ["W2", "BankStatement", "PayStub"]
    }
    response = client.post("/classify-document", json=payload)
    assert response.status_code == 200
    assert response.json() == expected
