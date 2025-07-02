from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from logger import logger
from  model import Base

import re

class Wine(Base):
    __tablename__= 'wine'

    id = Column("pk_produto",Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    # winery = Column(String(100), nullable=False)
    wine_type = Column(String(100), nullable=False)
    fixed_acidity = Column(Float, nullable=False)
    volatile_acidity = Column(Float, nullable=False)
    citric_acid = Column(Float, nullable=False)
    residual_sugar = Column(Float, nullable=False)
    chlorides = Column(Float, nullable=False)
    free_sulfur_dioxide = Column(Integer, nullable=False)
    total_sulfur_dioxide = Column(Integer, nullable=False)
    density = Column(Float, nullable=False)
    ph = Column(Float, nullable=False)
    sulphates = Column(Float, nullable=False)
    alcohol = Column(Float, nullable=False)
    quality = Column(String(20), nullable=False, default=0)  

    # __table_args__ = (
    #     UniqueConstraint('name', 'winery', 'type', name='uix_wine_name_winery_type'),
    # )

    def __init__(
        self,
        name: str,
        wine_type: str,
        fixed_acidity: float,
        volatile_acidity: float,
        citric_acid: float,
        residual_sugar: float,
        chlorides: float,
        free_sulfur_dioxide: int,
        total_sulfur_dioxide: int,
        density: float,
        ph: float,
        sulphates: float,
        alcohol: float,
        quality: str
    ):
        self.name = name
        self.wine_type = wine_type
        self.fixed_acidity = fixed_acidity
        self.volatile_acidity = volatile_acidity
        self.citric_acid = citric_acid
        self.residual_sugar = residual_sugar
        self.chlorides = chlorides
        self.free_sulfur_dioxide = free_sulfur_dioxide
        self.total_sulfur_dioxide = total_sulfur_dioxide
        self.density = density
        self.ph = ph
        self.sulphates = sulphates
        self.alcohol = alcohol
        self.quality = quality



