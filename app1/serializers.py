from rest_framework import serializers

from app1.models import Car
from core.models import Brand


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.StringRelatedField(read_only=True)
    acceleration = serializers.IntegerField(required=True)
    color = serializers.ChoiceField(choices=[
        ('BLK', 'Black'),
        ('GRE', 'Green'),
        ('BLU', 'Blue'),
        ('RED', 'Red'),
    ], allow_null=True, default=None)
    create_timestamp = serializers.DateTimeField(read_only=True)

    def update(self, instance: Car, validated_data: dict) -> Car:
        instance.brand = validated_data.get('brand', instance.brand)
        instance.acceleration = validated_data.get('acceleration', instance.acceleration)
        instance.color = validated_data.get('color', instance.color)
        return instance

    def create(self, validated_data: dict) -> Car:
        return Car.objects.create(**validated_data)
