import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices
from rest_framework.exceptions import ValidationError


class Location(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserRoles(TextChoices):
    ADMIN = 'admin', 'Администратор'
    MODERATOR = 'moderator', 'Модератор'
    MEMBER = 'member', 'Пользователь'


# User age validator
def validate_date(value: datetime.date):
    today = datetime.date.today()
    timedelta = datetime.timedelta(days=365 * 9)
    if value > today - timedelta:
        raise ValidationError('The user must be at least 9 years old!')


class User(AbstractUser):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    username = models.CharField(max_length=120, unique=True)
    password = models.CharField(max_length=120)
    email = models.EmailField(null=False, unique=True)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
    age = models.PositiveSmallIntegerField()
    birth_date = models.DateField(null=False, validators=[validate_date])
    location = models.ManyToManyField('Location')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
