import requests
from typing import List, Dict

# Define API base URL
BASE_URL = "http://127.0.0.1:8000"


# Product Search Tool
def search_products(query: str, max_price: int, size: str):
    response = requests.get(f"{BASE_URL}/search-products/",
                            params={"query": query, "max_price": max_price, "size": size})
    return response.json()


# Discount Checker Tool
def check_discount(code: str, price: int):
    response = requests.get(f"{BASE_URL}/apply-discount/", params={"code": code, "price": price})
    return response.json()


# Shipping Time Estimator Tool
def estimate_shipping(product_name: str, deadline: str):
    response = requests.get(f"{BASE_URL}/estimate-shipping/",
                            params={"product_name": product_name, "deadline": deadline})
    return response.json()


# Competitor Price Comparison Tool
def compare_prices(product_name: str):
    response = requests.get(f"{BASE_URL}/compare-prices/", params={"product_name": product_name})
    return response.json()


# Return Policy Checker Tool
def check_return_policy(website: str):
    response = requests.get(f"{BASE_URL}/return-policy/", params={"website": website})
    return response.json()
