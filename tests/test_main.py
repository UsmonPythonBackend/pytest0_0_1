from http.client import responses

import requests
import json
import pytest
import allure
from utils.main_page.api import get_active_items, get_cart, add_to_cart, get_smart_home, get_sports_shop, get_remont_store



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

@allure.parent_suite('Главная страница')
@allure.suite('Проверка добавления товаров в корзину у незарегистрированного пользователя')
@allure.title('Добавление товара в корзину')
def test_add_item():
    response = add_to_cart(cookie=cookie, offer_id=offer_id, condition_id=condition_id)
    assert response.status_code == 200


    response = response.json()
    print(json.dumps(response, indent=4))


@allure.parent_suite('Главная страница')
@allure.suite('Проверка перехода в раздел умный дом')
@allure.title("Получение session_id из cookie")
def test_get_smart_home():
    global cookie

    response = get_smart_home()

    assert response.status_code == 200


@allure.parent_suite('Главная страница')
@allure.suite('Проверка перехода в спортивные товары')
@allure.title("Получение session_id из cookie")
def test_get_sport_shop():
    global cookie

    response = get_sports_shop()

    assert response.status_code == 200


@allure.parent_suite('Главная страница')
@allure.suite('Проверка перехода в строительство и ремонт')
@allure.title("Получение session_id из cookie")
def test_get_remont_store():
    global cookie

    response = get_remont_store()

    assert response.status_code == 200
