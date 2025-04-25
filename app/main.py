from typing import Union
import json
from fastapi import FastAPI

app = FastAPI()

with open("resources/pokedex.json", encoding="utf-8") as f:
    pokedex = json.load(f)

@app.get("/pokemon/{id}")
def get_pokemon(id: int):
    result = next((poke for poke in pokedex if poke.get("id") == id), None)
    if result:
        return result
    return {"error": "Pokémon not found"}