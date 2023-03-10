from db import get_value, set_value
from repository import get_nif_datasource


def get_nif_repository(nif: str) -> dict:
    result = get_value(nif=nif)
    if result != None:
        return {"origin": "iFind", "data": {
            "nif": nif,
            "name": name
        }}
    else:
        name = get_nif_datasource(nif=nif)
        set_value(key=nif, value=name)
        return {"origin": "remote", "data": {
            "nif": nif,
            "name": name
        }}
