from rest_framework import serializers

from .models import Category, MenuItem, Cart

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ('id', 'title', 'price', 'stock', 'category', 'category_id')

class CartSerializer(serializers.ModelSerializer):
    # price = serializers.SerializerMethodField('calculate_price')
    class Meta:
        model = Cart
        fields = ('user', 'menu_item', 'quantity', 'unit_price', 'price')
        read_only_fields = ('user',  'price', 'unit_price')