from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Définir un modèle de données pour la réponse
class Message(BaseModel):
    message: str

@app.get("/flora-noubossi", response_model=Message)
async def read_flora_noubossi(param: str = "Hello, Flora Noubossi!"):
    """
    Endpoint qui retourne un message contenant le paramètre fourni.
    :param param: Le paramètre à retourner dans la réponse.
    :return: Message JSON contenant le paramètre.
    """
    return Message(message=param)

# Vous pouvez ajouter d'autres endpoints ici si nécessaire
