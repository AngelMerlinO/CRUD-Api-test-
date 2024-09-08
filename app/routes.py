from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from app.models import FlorResponse, FlorBase
from app.services import FlorService
from app.models import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todas las flores
@router.get("/flores", response_model=List[FlorResponse])
def obtener_flores(db: Session = Depends(get_db)):
    service = FlorService(db)  # Creación del servicio con la sesión
    return service.obtener_flores()

# Ruta para obtener una flor por ID
@router.get("/flores/{flor_id}", response_model=FlorResponse)
def obtener_flor(flor_id: int, db: Session = Depends(get_db)):
    service = FlorService(db)
    return service.obtener_flor_por_id(flor_id)

# Ruta para agregar una flor
@router.post("/flores", response_model=FlorResponse)
def agregar_flor(flor: FlorBase, db: Session = Depends(get_db)):
    service = FlorService(db)
    return service.agregar_flor(flor)

# Ruta para actualizar una flor
@router.put("/flores/{flor_id}", response_model=FlorResponse)
def actualizar_flor(flor_id: int, flor: FlorBase, db: Session = Depends(get_db)):
    service = FlorService(db)
    return service.actualizar_flor(flor_id, flor)

# Ruta para eliminar una flor
@router.delete("/flores/{flor_id}")
def eliminar_flor(flor_id: int, db: Session = Depends(get_db)):
    service = FlorService(db)
    return service.eliminar_flor(flor_id)
