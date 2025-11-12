import asyncio
import sys
from fastapi import FastAPI, HTTPException
from be.models.schemas import Credentials, AddToCartRequest
from be.services.sauce_service import login_user, get_product_details, add_to_cart
import traceback

# ✅ Fix for Playwright + FastAPI on Windows
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

app = FastAPI(title="SauceDemo Playwright API", version="1.0")

@app.post("/login")
async def login(creds: Credentials):
    try:
        return await login_user(creds.username, creds.password)
    except Exception as e:
        print("Login error:", repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/product/{name}")
async def get_product(name: str):
    try:
        return await get_product_details(name)
    except Exception as e:
        print("Product error:", repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/cart/add")
async def add_item_to_cart(req: AddToCartRequest):
    try:
        return await add_to_cart(req.item_name)
    except Exception as e:
        print("Cart error:", repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "SauceDemo Playwright API is running."}
