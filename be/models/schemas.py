# This file defines data models (schemas) for request and response validation using Pydantic.

from pydantic import BaseModel

class Credentials(BaseModel):
    # Schema for login credentials payload
    username: str
    password: str

class AddToCartRequest(BaseModel):
    # Schema for the "add to cart" request payload
    item_name: str
