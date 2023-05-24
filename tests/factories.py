import factory

from api.models import Ads
from users.models import User, UserRoles


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('user_name')
    password = factory.Faker('password')
    email = factory.Faker('email')
    role = UserRoles.MEMBER
    age = factory.Faker('pyint', min_value=9)
    birth_date = factory.Faker('date')


class AdsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ads

    name = factory.Faker('pystr', min_chars=10, max_chars=20)
    author = factory.SubFactory(UserFactory)
    price = factory.Faker('pyint', min_value=0)
    description = factory.Faker('sentence')
    is_published = False
