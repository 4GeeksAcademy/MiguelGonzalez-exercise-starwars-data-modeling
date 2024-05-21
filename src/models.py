import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'person'
    favorites = relationship("Favorites")
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    id = Column(Integer, primary_key=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    planetas = relationship("Planetas")
    personajes = relationship("Personajes")
    def to_dict(self):
        return {}

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    height = Column(String(100)) 
    mass = Column(String(100)) 
    hair_color = Column(String(100)) 
    eye_color = Column(String(100)) 
    birth_year = Column(String(100)) 
    gender = Column(String(100)) 

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    rotation_period = Column(String(100)) 
    orbital_period = Column(String(100)) 
    diameter = Column(String(100)) 
    climate = Column(String(100)) 
    gravity = Column(String(100)) 
    terrain = Column(String(100))
    surface_water = Column(String(100))
    population = Column(String(100))
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
