from fastapi import FastAPI
from pydantic import BaseModel

from agent import ask_agent
from tools import search_products, estimate_shipping, apply_discount, compare_prices, check_return_policy

app = FastAPI()


# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Virtual Shopping Assistant API"}


@app.get("/query/")
def query_agent(user_query: str):
    response = ask_agent(user_query)
    return {"response": response}


@app.get("/search-products/")
def search_products_api(query: str, max_price: float, size: str):
    results = search_products(query, max_price, size)
    return {"query_received": {"query": query, "max_price": max_price, "size": size}, "results": results}


@app.post("/estimate-shipping/")
def estimate_shipping_api(destination: str, deadline: str):
    result = estimate_shipping(destination, deadline)
    return result


@app.post("/check-discount/")
def check_discount_api(code: str, price: float):
    result = apply_discount(code, price)
    return result


@app.post("/compare-prices/")
def compare_prices_api(product_name: str):
    result = compare_prices(product_name)
    return result


@app.post("/check-return-policy/")
def check_return_policy_api(site: str):
    result = check_return_policy(site)
    return result


# Define request format
class QueryRequest(BaseModel):
    query: str


@app.post("/ask-agent/")
def ask_agent_api(request: QueryRequest):
    response = ask_agent(request.query)
    return {"response": response}
