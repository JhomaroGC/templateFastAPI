import fastapi

# importamos la instancia router de nuestro módulo users
from app.routers.users import router as users_router


app = fastapi.FastAPI(title="API template", version="0.0.1")


@app.get("/")
def root():
    return {"message": f"Bienvenido {app.title} version {app.version}"}


# Incluimos todas las rutas definidas en routers
app.include_router(users_router, prefix="/users", tags=["users"])
