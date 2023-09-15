from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy

NULLABLE = {
    'null': True,
    'blank': True
}

NOT_NULLABLE = {
    'null': False,
    'blank': False
}


class UserRoles(models.TextChoices):
    the_user = 'visitor', gettext_lazy('visitor')
    moderator = 'moderator', gettext_lazy('moderator')


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)
    role = models.CharField(max_length=20, **NULLABLE, choices=UserRoles.choices)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} {self.country}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


