from sklearn.model_selection import train_test_split
import joblib
import numpy as np

class PreProcessador:

    def __init__(self):
        """Inicializa o preprocessador, carregando o scaler treinado."""
        self.scaler = joblib.load(open('./machine_learning/pipeline/scaler_std.pkl', 'rb'))

    def separa_teste_treino(self, dataset, percentual_teste, seed=7):
        """Cuida de todo o pré-processamento: divisão em treino e teste."""
        X_train, X_test, Y_train, Y_test = self.__preparar_holdout(dataset,
                                                                   percentual_teste,
                                                                   seed)
        return (X_train, X_test, Y_train, Y_test)

    def __preparar_holdout(self, dataset, percentual_teste, seed):
        """Divide os dados em treino e teste usando o método holdout."""
        dados = dataset.values
        X = dados[:, 0:-1]
        Y = dados[:, -1]
        return train_test_split(X, Y, test_size=percentual_teste, random_state=seed)

    def preparar_form(self, form):
        """Prepara os dados recebidos do front para serem usados no modelo."""
        tipo_tinto = 1 if form.wine_type.lower() == 'red' else 0

        X_input = np.array([
            form.fixed_acidity,
            form.volatile_acidity,
            form.citric_acid,
            form.residual_sugar,
            form.chlorides,
            form.free_sulfur_dioxide,
            form.total_sulfur_dioxide,
            form.density,
            form.ph,
            form.sulphates,
            form.alcohol,
            tipo_tinto
        ]).reshape(1, -1)

        return X_input

    def padronizar_dados(self, X):
        """
        Aplica o scaler treinado aos dados.
        """
        return self.scaler.transform(X)
