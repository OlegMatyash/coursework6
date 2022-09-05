from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = (
            "email",
            "first_name",
            "last_name",
            "password",
            "phone",
        )


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            "first_name",
            "last_name",
            "phone",
        )
