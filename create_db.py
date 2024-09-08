from app.models import engine, Base

def inicializar_base_de_datos():
    # Crear todas las tablas definidas en los modelos (si no existen)
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas en la base de datos.")

if __name__ == "__main__":
    inicializar_base_de_datos()
