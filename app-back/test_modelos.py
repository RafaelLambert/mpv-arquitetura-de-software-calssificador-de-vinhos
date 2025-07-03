from model import *

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()
pipeline = Pipeline()

url_dados_normalizados = "./machine_learning/vinho_dataset/x_test_normalized.csv"
url_dados_padronizados = "./machine_learning/vinho_dataset/x_test_scaled.csv"
url_dados_resultados = "./machine_learning/vinho_dataset/y_test.csv"

# Colunas do dataset
# As colunas são as mesmas para ambos os datasets, pois o dataset já foi tratado e
colunas = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'tipo_tinto']


# Carga dos dados
dataset_normalizado = carregador.carregar_dados(url_dados_normalizados, colunas)
dataset_padronizado = carregador.carregar_dados(url_dados_padronizados, colunas)
dataset_resultados = carregador.carregar_dados(url_dados_resultados, ['qualidade_category'])

# Criar coluna booleana tipo_tinto (1 = tinto, 0 = branco) / Não necessário, pois o Data set já tratou esta condição.
# dataset['tipo_tinto'] = dataset['tipo'].apply(lambda x: 1 if x == 'red' else 0)
# dataset.drop(columns=['tipo'], inplace=True)

array_normalizado = dataset_normalizado.values
array_padronizado = dataset_padronizado.values

X_normalizado = dataset_normalizado
X_padronizado = dataset_padronizado
y_test = dataset_resultados

# Método para testar o modelo SVM a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_modelo_svm_std():  
    # Importando o modelo SVM
    model_path = './machine_learning/models/modelo_svm_std.pkl'
    modelo_svm = modelo.carrega_modelo(model_path)

    # Obtendo as métricas do SVM
    acuracia_svm = avaliador.avaliar(modelo_svm, X_padronizado, y_test)

    # Testando as métricas do SVM
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_svm >= 0.6
    # assert recall_svm >= 0.5
    # assert precisao_svm >= 0.5
    # assert f1_svm >= 0.5
    
def test_modelo_svm_norm():  
    # Importando o modelo SVM
    model_path = './machine_learning/models/modelo_svm_norm.pkl'
    modelo_svm = modelo.carrega_modelo(model_path)

    # Obtendo as métricas do SVM
    acuracia_svm = avaliador.avaliar(modelo_svm, X_normalizado, y_test)

    # Testando as métricas do SVM
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_svm >= 0.6
    # assert recall_svm >= 0.5
    # assert precisao_svm >= 0.5
    # assert f1_svm >= 0.5