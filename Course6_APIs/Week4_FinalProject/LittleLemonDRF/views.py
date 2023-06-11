from django.shortcuts import render
from rest_framework import generics

from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer

# CATEGORY VIEWS
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['title']

class SingleCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# MENU ITEM VIEWS
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'stock']
    filterset_fields = {'category': ['exact'], 
                        'price':['gte', 'lte']
                        }
    search_fields = ['title']

class MenuItemsSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer