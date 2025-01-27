import json
from products import Product
import dao

class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data):
        return Cart(
            id=data['id'],
            username=data['username'],
            contents=data['contents'],  # Avoid redundant product lookup here
            cost=data['cost']
        )


def get_cart(username: str) -> list[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    # Directly aggregate product IDs from all cart details
    items = []
    for cart_detail in cart_details:
        try:
            items.extend(json.loads(cart_detail['contents']))
        except json.JSONDecodeError:
            continue

    # Bulk-fetch products instead of individual lookups
    product_map = {p.id: p for p in dao.get_products_by_ids(items)}
    return [product_map[i] for i in items if i in product_map]


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)

