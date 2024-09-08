from sqlalchemy.orm import Session
from app.models import Flor

class FlorRepository:
    def __init__(self, db: Session):
        self.db = db

    def obtener_todas(self):
        return self.db.query(Flor).filter(Flor.disponible == True).all()

    def obtener_por_id(self, flor_id: int):
        return self.db.query(Flor).filter(Flor.id == flor_id).first()

    def agregar(self, flor: Flor):
        self.db.add(flor)
        self.db.commit()
        self.db.refresh(flor)
        return flor

    def actualizar(self, flor_id: int, flor_actualizada: Flor):
        flor = self.db.query(Flor).filter(Flor.id == flor_id).first()
        if flor:
            flor.nombre = flor_actualizada.nombre
            flor.descripcion = flor_actualizada.descripcion
            flor.cantidad = flor_actualizada.cantidad
            flor.disponible = flor_actualizada.disponible
            self.db.commit()
            self.db.refresh(flor)
            return flor
        return None

    def eliminar(self, flor_id: int):
        flor = self.db.query(Flor).filter(Flor.id == flor_id).first()
        if flor:
            self.db.delete(flor)
            self.db.commit()
            return True
        return False
