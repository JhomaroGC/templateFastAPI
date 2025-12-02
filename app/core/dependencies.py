from fastapi.security import OAuth2PasswordBearer

# Creamos una instancia de OAuth2PasswordBearer
# el tokenUrl es la ruta que se encarga de autenticar al usuario
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")
