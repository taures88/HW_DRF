from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import UserListView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListView.as_view()), # список пользователей
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # получение токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # обновление токена
]