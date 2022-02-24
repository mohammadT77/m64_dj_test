from rest_framework import serializers

from app1.models import Car, Address
from core.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

    car_set = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), many=True)
    # cars = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(),
    #                                           source='car_set',
    #                                           many=True)
    #
    # cars_count = serializers.IntegerField(source='car_set.count', read_only=True)


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = BrandSerializer(read_only=True)
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


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
