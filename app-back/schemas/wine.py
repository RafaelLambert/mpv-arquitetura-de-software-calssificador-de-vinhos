from pydantic import BaseModel
from typing import  List
from model.wine import Wine



class WineSchema(BaseModel):
    """
    Define como um novo vinho a ser inserido, deve ser representado
    """
    name:str = "Teste Ia Excelente"
    wine_type:str = "white"
    fixed_acidity:float = 6.5
    volatile_acidity:float = 0.16
    citric_acid:float = 0.33
    residual_sugar:float = 2.1
    chlorides:float = 0.045
    free_sulfur_dioxide:int = 15
    total_sulfur_dioxide:int = 45
    density:float = 0.9908
    ph:float = 3.3
    sulphates:float = 12.5
    alcohol:float = 12.5


class WineUpdateSchema(BaseModel):
    """
    Define o schema para atualizar as notas de um vinho.
    """
    name:str
    wine_type:str
    fixed_acidity:float
    volatile_acidity:float
    citric_acid:float
    residual_sugar:float
    chlorides:float
    free_sulfur_dioxide:int
    total_sulfur_dioxide:int
    density:float
    ph:float
    sulphates:float
    alcohol:float

class WineSearchSchema(BaseModel):
    """
    define como deve ser a estrutura que representa a busca que será
    feita apenas com base no nome do vinho    
    """
    name:str = "Santa vermelha"
    
def show_wines(wines:List[Wine]):
    """ 
    Retorna uma representação do vinho seguindo o schema definido em
    ProdutoViewSchema.
    """
    result = []
    for wine in wines:
        result.append({
            "id": wine.id,
            "name": wine.name,
            "wine_type": wine.wine_type,
            "fixed_acidity": wine.fixed_acidity,
            "volatile_acidity": wine.volatile_acidity,
            "citric_acid": wine.citric_acid,
            "density": wine.density,
            "ph": wine.ph,
            "alcohol": wine.alcohol,
            "quality": wine.quality
        })
    return {"wines":result}

class WineViewSchema(BaseModel):
    """ Define como um Vinho será retornado
    """
    id: int = 1
    name:str = "Santa Vermelha"    
    wine_type:str = "red"
    fixed_acidity:float = 0
    volatile_acidity:float = 0
    citric_acid:float = 0
    density:float = 0
    ph:float = 0
    alcohol:float = 0
    quality:str = "Ruim"
    

class WineDelSchema(BaseModel):
    """
    Define como deve ser a estrutura do dado retornado após uma requisição
    de remoção.
    """

    message: str
    name: str
    
def show_wine(wine:Wine):
    """
    Retorna uma representação do vinho seguindo o schema definido em
    WineViewSchema.        
    """
    return {        
        "id": wine.id,
        "name": wine.name,
        "wine_type": wine.wine_type,
        "fixed_acidity": wine.fixed_acidity,
        "volatile_acidity": wine.volatile_acidity,
        "citric_acid": wine.citric_acid,
        "density": wine.density,
        "ph": wine.ph,
        "alcohol": wine.alcohol,
        "quality": wine.quality
    }
            

class WineListSchema(BaseModel):
    """
    Define como uma listagem de vinhos será retornada.
    """
    winesList:List[WineViewSchema]