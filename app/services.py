from app.repositories import FlorRepository
from app.models import Flor, FlorBase
from sqlalchemy.orm import Session
from fastapi import HTTPException

class FlorService:
    def __init__(self, db: Session):
        self.repository = FlorRepository(db)

    def obtener_flores(self):
        return self.repository.obtener_todas()

    def obtener_flor_por_id(self, flor_id: int):
        flor = self.repository.obtener_por_id(flor_id)
        if not flor:
            raise HTTPException(status_code=404, detail="Flor no encontrada")
        return flor

    def agregar_flor(self, flor_data: FlorBase):
        nueva_flor = Flor(**flor_data.dict())
        return self.repository.agregar(nueva_flor)

    def actualizar_flor(self, flor_id: int, flor_data: FlorBase):
        flor_actualizada = Flor(**flor_data.dict())
        return self.repository.actualizar(flor_id, flor_actualizada)

    def eliminar_flor(self, flor_id: int):
        return self.repository.eliminar(flor_id)
