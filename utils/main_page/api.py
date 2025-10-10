import requests

from configs import base_url

# active_items_url = f"{base_url}/web/client/events/active"
# get_item = f"{base_url}/web/client/moderated-offers"
# search_url = f"{base_url}/web/client/search/full-text"
# get_cart_url = f"{base_url}/web/client/cart/view-cart/duplicate"
# add_cart_url = f"{base_url}/web/client/cart/moderated-items"

def get_active_items():
    response = requests.get(url=f"{base_url}/web/client/events/active")

    return response


def get_item(item_slug: str):
    response = requests.get(url=f"{base_url}/web/client/moderated-offers/{item_slug}")

    return response


def search_items(item_name: str):
    body = {
        "query": item_name
    }

    response = requests.post(url=f"{base_url}/web/client/search/full-text", json=body)

    return response

def get_cart(cookie=None):
    if cookie is None:
        response = requests.get(url=f"{base_url}/web/client/cart/view-cart/duplicate")
    else:
        headers = {
            "Cookie": f"cart={cookie};"
        }
        response = requests.get(url=f"{base_url}/web/client/cart/view-cart/duplicate", headers=headers)
    return response

get_cart()


def add_to_cart(cookie, offer_id: str, condition_id: id, quantity=1):
    headers = {
        "Cookie": f"cart={cookie};"
    }


    body = {
        "moderated_offer_id": offer_id,
        "condition_id": condition_id,
        "quantity": quantity
    }

    response = requests.post(
        url=f"{base_url}/web/client/cart/moderated-items",
        json=body,
        headers=headers
    )

    return response


def get_smart_home(cookie=None):
    if cookie is None:
        response = requests.get(url=f"{base_url}/web/client/filters/categories/umniy-dom/brands")
    else:
        headers = {
            "Cookie": f"cart={cookie};"
        }
        response = requests.get(url=f"{base_url}/web/client/filters/categories/umniy-dom/brands", headers=headers)
    return response

get_smart_home()


def get_sports_shop(cookie=None):
    if cookie is None:
        response = requests.get(url=f"{base_url}/web/client/filters/categories/sportivnie-tovari/brands")
    else:
        headers = {
            "Cookie": f"cart={cookie};"
        }
        response = requests.get(url=f"{base_url}/web/client/filters/categories/sportivnie-tovari/brands", headers=headers)
    return response

get_sports_shop()


def get_remont_store(cookie=None):
    if cookie is None:
        response = requests.get(url=f"{base_url}/web/client/filters/categories/stroiteljstvo-i-remont/brands")
    else:
        headers = {
            "Cookie": f"cart={cookie};"
        }
        response = requests.get(url=f"{base_url}/web/client/filters/categories/stroiteljstvo-i-remont/brands",
                                headers=headers)
    return response


get_remont_store()



