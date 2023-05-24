import pytest
from pytest_factoryboy import register

from tests.factories import AdsFactory, UserFactory

# Factories
register(AdsFactory)
register(UserFactory)


@pytest.fixture()
@pytest.mark.django_db
def token(client, django_user_model):
    username = "testuser"
    password = "testuser"
    role = 'member'
    age = 33
    birth_date = '1999-01-01'

    django_user_model.objects.create_user(
        username=username, password=password, role=role, age=age, birth_date=birth_date
    )

    response = client.post(
        "/user/token/",
        {"username": username, "password": password},
        format='json'
    )

    return response.data["access"]
