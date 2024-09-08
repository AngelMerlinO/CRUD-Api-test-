from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pydantic import BaseModel

# Información de conexión
MYSQL_HOST = 'localhost'
MYSQL_USER = 'floristeria_username'
MYSQL_PASSWORD = 'nueva_contraseña'
MYSQL_DB = 'floristeria'

# Crear la URL de conexión para SQLAlchemy
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"

# Base de SQLAlchemy
Base = declarative_base()

# Modelo SQLAlchemy para la tabla 'flores'
class Flor(Base):
    __tablename__ = "flores"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=True)
    cantidad = Column(Integer, nullable=False)
    disponible = Column(Boolean, nullable=False)

# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)

# Esquema de Pydantic para entrada y salida de datos (usado por FastAPI)
class FlorBase(BaseModel):
    nombre: str
    descripcion: str | None = None
    cantidad: int
    disponible: bool

# Clase para las respuestas de los endpoints (incluyendo ID)
class FlorResponse(FlorBase):
    id: int

    class Config:
        from_attributes = True  # Esto permite que Pydantic trabaje con objetos ORM (como SQLAlchemy)
