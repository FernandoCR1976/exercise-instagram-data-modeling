import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Login(Base):
    __tablename__ = 'Login'
    id = Column(Integer, primary_key=True)
    Nombre_Usuario = Column(String(20))
    Primer_Apellido = Column(String(20))
    Password = Column(String(20))

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    Nickname = Column(String(20))
    Correo = Column(String(20))
    Telefono = Column(String(8))
    Nombre_Usuario = Column(Integer, ForeignKey('Login.Nombre_Usuario'))
    Login = relationship(Login)

class Like(Base):
    __tablename__ = 'Like'
    id = Column(Integer, primary_key=True)
    CantidadLike = Column(Integer)
    NombreUsuario = Column(String(25))
    Nickname = Column(String(15))

class Publicacion(Base):
    __tablename__ = 'Publicacion'
    id = Column(Integer, primary_key=True)
    Titulo  = Column(String(15))
    Foto = Column(String(25))
    Texto = Column(String(50))
    CantidadLike = Column(Integer, ForeignKey('Like.CantidadLike'))
    Like = relationship(Like)

class Home(Base):
    __tablename__ = 'Home'
    id = Column(Integer, primary_key=True)
    N_Publicaciones = Column(Integer)
    N_Seguidos = Column(Integer)
    Biografia = Column(String(150))
    Publicacion_id = Column(Integer, ForeignKey('Publicacion.id'))
    Publicacion = relationship(Publicacion)
    Usuario_id = Column(Integer, ForeignKey('User.id'))
    Nickname = Column(Integer, ForeignKey('User.Nickname'))
    Nombre_Usuario = Column(Integer, ForeignKey('User.Nombre_Usuario'))
    User = relationship(User)

    
    





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')



## ForeignKey: Relación uno a muchos... (un carro tiene un fabricante, pero un fabricante puede tener muchos carros)
## Integer: Esto devuelve numeros enteros.
## Booleano: Una forma de representar datos binarios, es decir dos valores unicamente 0 y 1. (True es 1 y 0 es False).
