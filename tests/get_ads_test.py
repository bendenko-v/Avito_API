import pytest

from api.models import Ads, Category
from tests.factories import AdsFactory
from users.models import User


@pytest.mark.django_db
def test_ads_list_view(client, token):
    category = Category.objects.create(name='random_cat', slug='rslug')
    AdsFactory.create_batch(10, category=category)
    ads_count = Ads.objects.count()

    response = client.get(
        '/ad/',
        HTTP_AUTHORIZATION="Bearer " + token
    )

    assert response.status_code == 200
    assert len(response.data['results']) == ads_count


@pytest.mark.django_db
def test_ad_detail_view(client, token):
    category = Category.objects.create(name='random_cat', slug='rslug')
    ads = AdsFactory.create_batch(3, category=category)
    ad_id = ads[0].id

    response = client.get(
        f'/ad/{ad_id}/',
        HTTP_AUTHORIZATION="Bearer " + token
    )

    assert response.status_code == 200
    assert response.data['id'] == ad_id


@pytest.mark.django_db
def test_ad_create_view(client, token):
    category = Category.objects.create(name='Flowers', slug='plants')
    user = User.objects.get(username='testuser')

    data = {
        "name": "Цветок красивый",
        "price": 333,
        "description": "Garden Best flower",
        "category": category.id
    }

    expected_response = {
        "name": "Цветок красивый",
        "price": 333,
        "description": "Garden Best flower",
        "is_published": False,
        "image": None,
        "author": user.id,
        "category": category.id
    }

    response = client.post(
        '/ad/create/',
        data=data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + token
    )
    response.data.pop('id')

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_selection_create_view(client, token):
    category = Category.objects.create(name='random_cat', slug='rslug')
    ads = AdsFactory.create_batch(3, category=category)
    user = User.objects.get(username='testuser')
    ads_id = [ad.id for ad in ads]

    data = {
        "name": "My new selection!",
        "items": [
            ads_id[0],
            ads_id[1],
            ads_id[2],
        ]
    }

    expected_response = {
        "name": "My new selection!",
        "owner": user.id,
        "items": [
            ads_id[0],
            ads_id[1],
            ads_id[2],
        ]
    }

    response = client.post(
        '/selection/create/',
        data=data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + token
    )

    assert response.status_code == 201
    assert response.data == expected_response
