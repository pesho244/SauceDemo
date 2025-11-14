# be/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from be.services.sauce_service import (
    login_user,
    get_product_details,
    add_to_cart,
    checkout_order
)

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(req: LoginRequest):
    return await login_user(req.username, req.password)

@app.get("/product/{name}")
async def product(name: str):
    return await get_product_details(name)

@app.post("/cart/{name}")
async def cart(name: str):
    return await add_to_cart(name)

#  Checkout endpoint — you did NOT add this before!
@app.post("/checkout/{item_name}")
async def checkout(item_name: str, first: str, last: str, zip: str):
    return await checkout_order(first, last, zip, item_name)
