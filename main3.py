#2.12.2024
from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

# Список для зберігання імен
names_list = []

@app.post("/add_name/")
def add_name(name: str):
    """Додає нове ім'я до списку."""
    if name in names_list:
        raise HTTPException(status_code=400, detail="Name already exists.")
    names_list.append(name)
    return {"message": f"Name '{name}' added successfully."}

@app.get("/get_names/", response_model=List[str])
def get_names():
    """Повертає список всіх збережених імен."""
    return names_list

@app.delete("/delete_name/")
def delete_name(name: str):
    """Видаляє ім'я зі списку."""
    if name not in names_list:
        raise HTTPException(status_code=404, detail="Name not found.")
    names_list.remove(name)
    return {"message": f"Name '{name}' deleted successfully."}

