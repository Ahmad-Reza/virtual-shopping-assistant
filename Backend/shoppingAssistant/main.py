import random
from datetime import datetime, timedelta

from fastapi import FastAPI
from pydantic import BaseModel

from agent import agent

app = FastAPI()

# Sample product database (Replace this with a real database or API call)
PRODUCTS = [
    {"name": "Floral Skirt", "price": 35, "size": "S", "stock": True},
    {"name": "White Sneakers", "price": 65, "size": "8", "stock": True},
    {"name": "Casual Denim Jacket", "price": 80, "size": "M", "stock": False},
]

# Sample discount codes
DISCOUNTS = {"SAVE10": 10, "FASHION20": 20}

# Sample competitor prices
COMPETITOR_PRICES = {
    "Casual Denim Jacket": {"SiteA": 80, "SiteB": 75, "SiteC": 70},
    "White Sneakers": {"SiteA": 70, "SiteB": 65, "SiteC": 68}
}

# Sample return policies
RETURN_POLICIES = {"SiteA": "30-day return", "SiteB": "No returns", "SiteC": "15-day return"}


# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Virtual Shopping Assistant API"}


# API 1: Search for products
@app.get("/search-products/")
def search_products_api(query: str, max_price: int, size: str):
    filtered_products = [
        product for product in PRODUCTS
        if query.lower() in product["name"].lower() and product["price"] <= max_price and product["size"] == size
    ]

    return {"products": filtered_products}


# API 2: Apply discount code
@app.post("/apply-discount/")
def check_discount_api(code: str, price: float):
    discount_amount = DISCOUNTS.get(code, 0)
    final_price = price - discount_amount
    return {"final_price": final_price, "discount_applied": discount_amount > 0}


# API 3: Estimate shipping
@app.post("/estimate-shipping/")
def estimate_shipping_api(destination: str, deadline: str):
    estimated_days = random.randint(2, 7)
    estimated_date = datetime.today() + timedelta(days=estimated_days)

    return {
        "delivery_date": estimated_date.strftime("%Y-%m-%d"),
        "estimated_days": estimated_days,
        "cost": random.randint(5, 15)
    }


# API 4: Compare prices with competitors
@app.post("/compare-prices/")
def compare_prices_api(product_name: str):
    prices = COMPETITOR_PRICES.get(product_name, {})
    return [{"site": site, "price": price} for site, price in prices.items()]


# API 5: Get return policy for a site
@app.get("/return-policy/")
def get_return_policy(site: str):
    policy = RETURN_POLICIES.get(site, "Unknown")
    return {"site": site, "policy": policy}


# Define request format
class UserQuery(BaseModel):
    query: str


# API Endpoint to Call AI Shopping Assistant
@app.post("/assistant/")
def shopping_assistant(user_query: UserQuery):
    response = agent.run(user_query.query)  # Let the agent decide the best action
    return {"response": response}
