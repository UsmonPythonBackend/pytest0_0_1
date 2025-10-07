from http.client import responses

import requests
import json
import pytest
import allure
from utils.main_page.api import get_active_items, get_cart, add_to_cart, search_items



@allure.parent_suite('Главная страница')
@allure.suite('Проверка добавления товара в Корзину у незарегистрировааного пользователя')
@allure.title("Получение товаров")
def test_get_active_items():
    global offer_id, slug, condition_id

    response = get_active_items()
    assert response.status_code == 200
    response = response.json()
    assert len(response) > 0


    first_item = response[0]["offers"][0]

    offer_id = first_item["moderated_offer_id"]
    slug = first_item["slug"]
    condition_id = first_item["condition"]["id"]


@allure.parent_suite('Главная страница')
@allure.suite('Проверка добавления товара в Корзину у незарегистрировааного пользователя')
@allure.title("Получение session_id из cookie")
def test_get_session_id():
    global cookie

    response = get_cart()

    assert response.status_code == 200

    cookie = response.cookies.get_dict()['cart']
    assert isinstance(cookie, str), f'Тип куки на самом деле {type(cookie)}'
#
# @allure.parent_suite('Главная страница')
# @allure.suite('Проверка добавления товаров в корзину у незарегистрированного пользователя')
# @allure.title('Добавление товара в корзину')
def test_add_item():
    response = add_to_cart(cookie=cookie, offer_id=offer_id, condition_id=condition_id)
    assert response.status_code == 200



    response = response.json()
    print(json.dumps(response, indent=4))




# @pytest.mark.parametrize('item', ['iphone', 'samsung', 'xiaomi'])
# def test_search(item):
#     search_body = {
#         "query": item
#     }
#     response = requests.post(url=search_url, json=search_body)
#     res_json = response.json()
#
#     items_list = res_json["items"]
#
#     print(f'{items_list}\n\n')
#
#     assert response.status_code == 200
#     assert len(items_list) > 0 , "Ничего нет"
#

#    print(json.dumps(res_json, indent=2))

# def url_generator(slug):
#     return
