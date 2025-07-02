import os
os.environ['FLASK_ENV'] = 'testing'  # Define o ambiente de teste para o Flask

import pytest
import json
from app import app
from model import Session, Wine, Base, engine

# To run: pytest -v test_api.py

@pytest.fixture
def client():
    """Configura o cliente de teste para a aplicação Flask"""
    
    # Garante que as tabelas estão criadas no banco em memória
    Base.metadata.create_all(bind=engine)

    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def clear_database():
    session = Session()
    session.query(Wine).delete()
    session.commit()
    session.close()


@pytest.fixture
def sample_wine_data():
    return {
        "name": "Teste Ia Excelente",
        "wine_type": "white",
        "fixed_acidity": 6.5,
        "volatile_acidity": 0.16,
        "citric_acid": 0.33,
        "residual_sugar": 2.1,
        "chlorides": 0.045,
        "free_sulfur_dioxide": 15,
        "total_sulfur_dioxide": 45,
        "density": 0.9908,
        "ph": 3.3,
        "alcohol": 12.5,
        "quality": "Razoável"
    }    


def test_get_wines(client):
    response = client.get('/wines')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'wines' in data  # Verifica se a chave existe
    assert isinstance(data['wines'], list)  # Verifica se o valor é uma lista

def test_get_wine(client, sample_wine_data):
    # Primeiro, insere o vinho
    client.post('/wine',
                json=sample_wine_data,
                content_type='application/json')

    response = client.get('/wine?name=Teste%20Ia%20Excelente')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'name' in data
    assert data['name'] == 'Teste Ia Excelente'


def test_add_duplicate_wine(client, sample_wine_data):
    """Testa a adição de um vinho duplicado"""
    # Primeiro adiciona o vinho
    client.post('/wine', 
                json=sample_wine_data,
                content_type='application/json')
    
    # Tenta adicionar novamente
    response = client.post('/wine', 
                          json=sample_wine_data,
                          content_type='application/json')
    
    assert response.status_code == 409
    data = json.loads(response.data)
    assert 'message' in data
    assert data['message'] == 'vinho de mesmo nome já salvo na base :/'
