from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator


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
    user = serializers.PrimaryKeyRelatedField(read_only=True,
                                              default=serializers.CurrentUserDefault(),)
    # menu_item = serializers.StringRelatedField()
    class Meta:
        model = Cart
        fields = ('user', 'menu_item', 'quantity', 'unit_price', 'price')
        read_only_fields = ('unit price', 'price')
        validators = [UniqueTogetherValidator(queryset=Cart.objects.all(),
                                            fields=['user', 'menu_item'])]