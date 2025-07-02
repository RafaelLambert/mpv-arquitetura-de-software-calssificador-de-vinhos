import joblib

class Pipeline:
    
    def __init__(self):
        """Inicializa o pipeline"""
        self.pipeline = None
    
    def carrega_pipeline(self, path):
        """Carregamos o pipeline construído durante a fase de treinamento
        """
        
        with open(path, 'rb') as file:
             self.pipeline = joblib.load(file)
        return self.pipeline