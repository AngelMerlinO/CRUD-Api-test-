from fastapi import FastAPI
from app.routes import router as flor_router

app = FastAPI()

# Registrar las rutas de las flores
app.include_router(flor_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
