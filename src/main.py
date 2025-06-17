A especificação fornecida parece estar um pouco confusa, você pediu uma API em Node.js, no entanto, as instruções iniciais pedem uma implementação em Python usando FastAPI e Pydantic. Vou supor que você queira uma API em Python. Infelizmente, sem mais detalhes sobre os endpoints, eu só posso fornecer um exemplo genérico. Aqui está um exemplo de como isso poderia ser feito:


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float


items = {}

@app.post("/items/")
async def create_item(item: Item):
    """
    Create an item with all the information:
    - **name**: each item must have a name
    - **description**: a short description of the item
    - **price**: the price of the item
    """
    if item.name in items:
        raise HTTPException(status_code=400, detail="Item already exists")

    items[item.name] = item
    return item


@app.get("/items/{item_name}")
async def read_item(item_name: str):
    """
    Get item by name.
    - **item_name**: the name of the item to get
    """
    item = items.get(item_name)
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return item

Este código define uma API FastAPI com dois endpoints. O primeiro endpoint permite criar um novo item com as propriedades `name`, `description` e `price`. O segundo endpoint permite obter um item existente pelo nome. Se um item com o nome fornecido não existir, um erro 404 será retornado.