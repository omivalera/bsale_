from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    '''
    Output example:
    {
        id : 01,
        name : bebida
    }
    '''
    class Meta:
        model = Category
        fields = [
            'id',
            'name']
        

class ProductSerializer(serializers.ModelSerializer):
    '''
    Output example:
    {
            "id": 68,
            "name": "Bebida Sprite 1 Lt",
            "url_image": null,
            "price": 1250.0,
            "discount": 10,
            "category": {
                "id": 4,
                "name": "bebida"
            }
        },
    '''
    category = CategorySerializer(many = False)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'url_image',
            'price',
            'discount',
            'category'
        ]

class GroupSerializer(serializers.ModelSerializer):
    '''
    Output example:
    {
            "bebida energetica": [
                {
                    "id": 5,
                    "name": "ENERGETICA MR BIG",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/misterbig3308256.jpg",
                    "price": 1490.0,
                    "discount": 20,
                    "category_id": 1
                },
                ...
    '''
    def to_representation(self, data):
        rep = { data.name : [prod for prod in Product.objects.filter(category_id=data.id).values()] }
        return rep

    class Meta:
        model = Product
        fields = '__all__'

