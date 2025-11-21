import os
import requests

BASE_URL = "http://127.0.0.1:8000"
PRODUCT = "Sauce Labs Bolt T-Shirt"

# ---------------------------
# Load API credentials safely
# ---------------------------
USERNAME = os.getenv("SAUCE_API_USERNAME")
PASSWORD = os.getenv("SAUCE_API_PASSWORD")

if not USERNAME or not PASSWORD:
    raise Exception("Missing environment variables SAUCE_API_USERNAME / SAUCE_API_PASSWORD")


def test_login():
    print("\n--- LOGIN ---")
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    r = requests.post(f"{BASE_URL}/login", json=payload)
    print("Login →", r.status_code, r.json())


def test_product():
    print("\n--- GET PRODUCT ---")
    r = requests.get(f"{BASE_URL}/product/{PRODUCT.replace(' ', '%20')}")
    print("Product →", r.status_code, r.json())


def test_add_to_cart():
    print("\n--- ADD TO CART ---")
    r = requests.post(f"{BASE_URL}/cart/{PRODUCT.replace(' ', '%20')}")
    print("Add to cart →", r.status_code, r.json())


def test_checkout():
    print("\n--- CHECKOUT ---")

    params = {
        "first": "John",
        "last": "Doe",
        "zip": "12345"
    }

    r = requests.post(
        f"{BASE_URL}/checkout/{PRODUCT.replace(' ', '%20')}",
        params=params
    )

    print("Checkout →", r.status_code, r.json())


if __name__ == "__main__":
    test_login()
    test_product()
    test_add_to_cart()
    test_checkout()
