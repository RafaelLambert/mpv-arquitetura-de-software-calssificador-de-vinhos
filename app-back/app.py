from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect,Flask
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import *
from logger import logger
from schemas import WineSchema, WineUpdateSchema, WineSearchSchema, WineViewSchema, WineListSchema, WineDelSchema,\
                            show_wines, show_wine, show_wines
from schemas.error import ErrorSchema
from flask_cors import CORS



info = Info(title="API-Stdent", version="0.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

#definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
wine_tag = Tag(name="Wine", description="Tela de cadastro, visualização e consulta de um Vinho. Também é possivel verificar a qualidade classificada automáticament a partir dos atributos de cadastro")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para o index.html do frontend."""
    return redirect("/app-front/index.html")

# Rota para documentação OpenAPI
@app.get("/docs", tags=[home_tag])
def docs():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect("/openapi")

@app.post('/wine', tags=[wine_tag],
          responses={"200":WineViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def predict(form: WineSchema):
    """Adiciona um novo Vinho à base de dados

    Retorna uma representação dos vinhos e a classificação associada.
    """

    logger.info(form)

    # Instanciando classes
    preprocessador = PreProcessador()
    pipeline = Pipeline()

    # Preparando os dados para o modelo
    X_input = preprocessador.preparar_form(form)
    # Carregando modelo
    model_path = "./machine_learning/pipeline/modelo_svm_std.pkl"
    modelo = pipeline.carrega_pipeline(model_path)
    # Realizando a predição
    outcome = int(modelo.predict(X_input)[0])

    if outcome == 0:
        outcome = "Ruim"
    elif outcome == 1:
        outcome = "Razoável"
    elif outcome == 2:
        outcome = "Bom"
    elif outcome == 3:
        outcome = "Excelente"

    print(f"Resultado da predição: {outcome}")

    # Criando o objeto Wine
    wine = Wine(
        name = form.name,
        wine_type = form.wine_type,
        fixed_acidity = form.fixed_acidity,
        volatile_acidity = form.volatile_acidity,
        citric_acid = form.citric_acid,
        residual_sugar = form.residual_sugar,
        chlorides = form.chlorides,
        free_sulfur_dioxide = form.free_sulfur_dioxide,
        total_sulfur_dioxide = form.total_sulfur_dioxide,
        density = form.density,
        ph = form.ph,
        sulphates = form.sulphates,
        alcohol = form.alcohol,
        quality = outcome
    )

    logger.info(f"Recebido: name={form.name}, cpf={form.wine_type}, grade_level={form.alcohol}")
    logger.warning(f"Adicionando vinho de nome: '{wine.name}'")

    try:
        # criando conexão com a base
        session = Session()
        logger.warning(session)
        # adicionando wine
        session.add(wine)
        logger.warning(wine)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.warning(f"Adicionado vinho de nome: '{wine.name}'")
        return show_wine(wine), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "vinho de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar vinho '{wine.name}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo vinho :/"
        logger.warning(f"Erro ao adicionar vinho '{wine.name}', {error_msg}")
        return {"message": error_msg}, 400

@app.get('/wines', tags=[wine_tag],
          responses={"200":WineListSchema, "409": ErrorSchema, "400": ErrorSchema})
def get_wines():
    """Faz a busca por todos os vinhos cadastrados

    Retorna uma representação da listagem de vinhos.
    """
    logger.debug(f"Coletando vinhos")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    wines = session.query(Wine).all()

    if not wines:
        # se não há produtos cadastrados
        return {"wines": []}, 200
    else:
        logger.debug(f"%d vinhos econtrados" % len(wines))
        # retorna a representação de produto
        print(wines)
        return show_wines(wines), 200
    
@app.get('/wine', tags=[wine_tag],
         responses={"200": WineViewSchema, "404": ErrorSchema})
def get_wine(query: WineSearchSchema):
    """Faz a busca por um Vinho a partir do id do wine

    Retorna uma representação dos vinhos e comentários associados.
    """
    wine_name = query.name
    logger.debug(f"Coletando dados sobre vinho #{wine_name}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    wine = session.query(Wine).filter(Wine.name == wine_name).first()

    if not wine:
        # se o wine não foi encontrado
        error_msg = "Vinho não encontrado na base :/"
        logger.warning(f"Erro ao buscar vinho '{wine_name}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Vinho econtrado: '{wine.name}'")
        # retorna a representação de wine
        return show_wine(wine), 200
    
@app.delete('/wine', tags=[wine_tag],
            responses={"200": WineViewSchema,"404": ErrorSchema})    
def del_wine(query: WineSearchSchema):
    """Deleta um Vinho a partir do nome informado

    Retorna uma mensagem de confirmação da remoção.
    """
    wine_name = unquote(unquote(query.name))
    print(wine_name)
    logger.debug(f"Deletando dados sobre o vonho #{wine_name}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Wine).filter(Wine.name == wine_name).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado vinho #{wine_name}")
        return {"message": "Wine removido", "name": wine_name}
    else:
        # se o produto não foi encontrado
        error_msg = "Vinho não encontrado na base :/"
        logger.warning(f"Erro ao deletar vinho #'{wine_name}', {error_msg}")
        return {"message": error_msg}, 404
