from fastapi import FastAPI
from app.routers.usuario_routers import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def root():
    return {"mensagem": "rodando!"}