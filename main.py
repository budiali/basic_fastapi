from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.base import BaseHTTPMiddleware

# membuat aplikasi FastAPI
app = FastAPI()

# membuat middleware
@app.middleware("http")
async def add_process_time_header(request, call_next):
    reponse = await call_next(request)
    reponse.headers["X-Process-Time"] = str(10.5)
    return reponse

# Model Pydantic untuk validasi data input
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# membuat route (endpoint) pertama
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# membuat endpoint dengan parametr
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Endpoint untuk menerima data JSON
@app.post("/items/")
def create_item(item:Item):
    return {"name": item.name, "price": item.price}