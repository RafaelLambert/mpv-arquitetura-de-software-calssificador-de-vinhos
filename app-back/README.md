# MVP Classificador de Vinhos - PUC-Rio

Este repositório contém o back-end do projeto MVP proposto pela PUC-Rio. A solução foi desenvolvida utilizando Python com Flask para construção de uma API REST integrada a um modelo de classificação treinado. O foco do projeto é oferecer um sistema que permita o cadastro de vinhos, classificação automática com base em atributos físico-químicos e gerenciamento das informações cadastradas.

O objetivo deste projeto é demonstrar habilidades no desenvolvimento de uma API REST documentada, capaz de integrar um modelo de Machine Learning e que possa ser consumida posteriormente por um Front-End.

---

## 🤖 Sobre o Modelo de Machine Learning

O modelo utilizado para classificar os vinhos foi o **SVM (Support Vector Machine) com dados padronizados**, que apresentou um desempenho satisfatório durante os testes de validação. Os hiperparâmetros definidos para o modelo final foram:

-`C = 10`

-`kernel = 'rbf'`

-`gamma = 'scale'`

O modelo foi treinado com dados físico-químicos de vinhos segundos os dois dataset:

- `winequality-red-training-test-model.csv`
- `winequality-white-training-test-model.csv`

Após treinado, o modelo foi integrado ao back-end por meio de um pipeline serializado em `.pkl`, exportado utilizando o joblib.

## 🧩 Funcionalidades Principais

- **Cadastro de Vinhos**: Permite registrar vinhos com características específicas como acidez, álcool, pH, tipo, entre outros.

- **Classificação Automática**: Um modelo de aprendizado de máquina classifica automaticamente o vinho como _Ruim_, _Razoável_, _Bom_ ou _Excelente_ com base nos atributos informados.

- **Consulta de Vinhos**: Permite listar todos os vinhos ou buscar individualmente por nome.

- **Remoção de Vinhos**: Remove registros de vinhos do banco de dados.

---

## 🚀 Tecnologias Utilizadas

- **Linguagem**: Python

- **Framework**: Flask

- **Banco de Dados**: SQLite (via SQLAlchemy)

- **Validação de Dados**: Pydantic

- **Documentação da API**: flask-openapi3 (OpenAPI/Swagger)

- **Controle de CORS**: Flask-CORS

- **Machine Learning**: scikit-learn

- **Serialização de Modelos**: joblib

---

## 📌 Endpoints da API

### 1. Documentação

- **Rota**: `/`

- **Método**: `GET`

- **Descrição**: Redireciona para a interface de documentação (Swagger, Redoc ou RapiDoc).

### 2. Cadastro de Vinhos

- **Rota**: `/wine`

- **Método**: `POST`

- **Descrição**: Adiciona um novo vinho à base de dados e retorna a classificação automática.

- **Corpo de Exemplo**:

```json

{

  "name": "Santa Vermelha",

  "wine_type": "red",

  "fixed_acidity": 7.0,

  "volatile_acidity": 0.5,

  "citric_acid": 0.3,

  "residual_sugar": 2.0,

  "chlorides": 0.045,

  "free_sulfur_dioxide": 15,

  "total_sulfur_dioxide": 45,

  "density": 0.9908,

  "ph": 3.3,

  "sulphates": 0.65,

  "alcohol": 12.0

}


```

### 3. Listagem de Vinhos

***Rota** : `/wines`

***Método** : `GET`

***Descrição** : Retorna a lista completa de vinhos cadastrados.

### 4. Busca Individual de Vinho

***Rota** : `/wine`

***Método** : `GET`

***Descrição** : Busca um vinho pelo nome.

***Parâmetros de Query** :

*`name`: Nome do vinho

### 5. Remoção de Vinho

***Rota** : `/wine`

***Método** : `DELETE`

***Descrição** : Remove um vinho da base de dados com base no nome informado.

***Parâmetros de Query** :

*`name`: Nome do vinho

---

## ⚙️ Como Executar o Projeto

### 🔧 Pré-requisitos

***Python 3.10+**

***pip (Python Package Installer)**

### 📥 Passos

1.**Verifique se o Python está instalado** :
```
python --version
```

2.**Verifique se o pip está instalado** :
```
pip --version
```

3.**Clone o repositório** :
```
git clone <https://github.com/SEU_USUARIO/seu-repo-classificador-de-vinhos>

cd seu-repo-classificador-de-vinhos
```
4.**Crie e ative um ambiente virtual** :
```
python -m venv env

# No Windows

env\Scripts\activate

# No Linux/Mac

source env/bin/activate
```

5.**Instale as dependências** :
```
pip install -r requirements.txt
```

6.**Execute a aplicação** :
```
flask run --host 0.0.0.0 --port 5000

```

A aplicação estará disponível em [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Testes

Os testes podem ser executados com `pytest`:
```
pytest -v (arquivo de teste)
```

Os seguintes testes estão disponíveis:

* Testes da API (`test_api.py`)
* Testes do modelo de classificação (`test_modelos.py`)

---

## 📄 Licença

Este projeto foi desenvolvido como parte de um MVP para a PUC-Rio e é de uso educacional.
