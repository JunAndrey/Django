from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['stock', 'product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']
        
    def validate(self, attrs):
        if not attrs['positions'][0]:
            raise ValidationError('Список пуст!')
        return attrs 

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for position in positions:
            StockProduct.objects.create(stock_id=stock.pk, **position)

        return stock

    def update(self, instance, validated_data):
        positions_data = validated_data.pop('positions')
        print(positions_data)
        positions = instance.positions.all()
        print(positions)
        stock = super(StockSerializer, self).update(instance, validated_data)
        for position in positions_data:
            print(position)
            StockProduct.objects.update_or_create(
                stock_id=stock.pk, **position)
        return stock
