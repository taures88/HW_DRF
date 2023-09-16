from rest_framework import serializers

from users.models import User


"""класс сериализатор для пользователя"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'