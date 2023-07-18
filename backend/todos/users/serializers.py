from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

    def create(self, validated_data):
        return User.objects.create(
            username=validated_data["username"],
            password=make_password(validated_data["password"]),
        )


class UserListSerializer(serializers.ModelSerializer):
    todos = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='description'
     )

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'todos'
        ]


class UserUpdateSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(
        max_length=255, min_length=6, write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = User
        fields = [
            'username',
            'new_password',
        ]

    def update(self, instance, validated_data):
        if validated_data.get("new_password"):
            instance.password = make_password(validated_data["new_password"])
        instance.username = validated_data["username"]
        instance.save()
        return instance

