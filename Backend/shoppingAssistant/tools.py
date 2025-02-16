# tools.py
from typing import List, Dict


def search_products(name: str, price: float, size: str) -> List[Dict]:
    """Mock function to search for fashion products."""
    return [
        {"name": name, "price": 35, "size": size, "available": True},
        {"name": "Alternative " + name, "color": "Blue", "price": 38, "size": "M", "available": False}
    ]


def estimate_shipping(location: str, delivery_date: str) -> Dict:
    """Mock function to estimate shipping time & cost."""
    return {
        "location": location,
        "estimated_cost": 5.99,
        "estimated_delivery": delivery_date
    }


def apply_discount(promo_code: str, base_price: float) -> Dict:
    """Mock function to validate promo codes."""
    discount = 10 if promo_code == "SAVE10" else 0
    final_price = base_price - (base_price * discount / 100)
    return {"promo_code": promo_code, "discount_applied": discount, "final_price": final_price}


def compare_prices(product_name: str) -> List[Dict]:
    """Mock function to compare prices across different stores."""
    return [
        {"store": "StoreA", "price": 80},
        {"store": "StoreB", "price": 75},
        {"store": "StoreC", "price": 78}
    ]


def check_return_policy(store_name: str) -> Dict:
    """Mock function to return store's return policy."""
    policies = {
        "StoreA": "30-day return policy with free returns.",
        "StoreB": "14-day return policy, return shipping costs apply.",
        "StoreC": "No returns on discounted items."
    }
    return {"store": store_name, "return_policy": policies.get(store_name, "Return policy not found.")}
