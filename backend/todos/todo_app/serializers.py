from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=255)
    complete_date = serializers.DateField()
    is_expired = serializers.BooleanField(default=False)
    is_done = serializers.BooleanField(default=False)


    def create(self, validated_data):
        return Todo(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data['description']
        instance.complete_date = validated_data['complete_date']
        instance.is_expired = validated_data['is_expired']
        instance.is_done = validated_data['is_done']
        return instance


class TodoListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField(max_length=255)
    complete_date = serializers.DateField()
    is_expired = serializers.BooleanField(default=False)
    is_done = serializers.BooleanField(default=False)