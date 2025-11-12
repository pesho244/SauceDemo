import requests

BASE_URL = "http://127.0.0.1:8000"

def test_api_endpoints():
    # 1 Test login
    login_payload = {
        "username": "standard_user",
        "password": "secret_sauce"
    }
    login_res = requests.post(f"{BASE_URL}/login", json=login_payload)
    print("Login:", login_res.json())

    # 2 Test get product
    product_res = requests.get(f"{BASE_URL}/product/Sauce%20Labs%20Backpack")
    print("Product:", product_res.json())

    # 3 Test add to cart
    add_payload = {"item_name": "Sauce Labs Backpack"}
    add_res = requests.post(f"{BASE_URL}/cart/add", json=add_payload)
    print("Add to cart:", add_res.json())

if __name__ == "__main__":
    test_api_endpoints()