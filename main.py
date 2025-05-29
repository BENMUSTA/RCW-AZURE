from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware 
#permet de gérer les requêtes cross-origin
#cors est un mécanisme de sécurité qui permet de contrôler les ressources partagées entre différentes origines (domaines, protocoles, ports)

app = FastAPI()

@app.get("/")
async def bienvenue():
    try:
        return {"message": "Hello, World!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/test")
async def bienvenueserveur():
    try:
        return {"message": "Hello, serveur"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))