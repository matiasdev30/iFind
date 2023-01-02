import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def get_nif_datasource(nif: str) -> str :
    response = requests.get(os.environ["BASE_URL"] + nif, headers=headers)
    data = json.loads(response.text)
    if("message" in data):
        raise Exception("Nif invalido")
    return data["nome"]
   



