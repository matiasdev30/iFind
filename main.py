import fastapi
from repository import get_nif_repository

app = fastapi.FastAPI()

@app.get("/")
def root():
    return {"msg" : "Bem-Vindo ao iFind"}

@app.get("/find_user/")
def find_user(nif: str):
    try:
        data = get_nif_repository(nif=nif)
        print(data)
        return data
    except BaseException as e :
        raise fastapi.HTTPException(status_code=404, detail=e.__str__())
    