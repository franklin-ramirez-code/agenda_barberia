import json

ARCHIVO = 'citas.json'

def cargar_citas() -> list:
    try:
        with open (ARCHIVO, 'r', encoding = 'utf-8') as archivo:
            citas = json.load(archivo)
            return citas
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def guardar_cita(citas: list) -> None:
    with open (ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump(citas, archivo, indent=4, ensure_ascii=False)