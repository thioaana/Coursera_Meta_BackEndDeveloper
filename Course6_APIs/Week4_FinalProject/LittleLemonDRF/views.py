from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser



from .models import Category, MenuItem, Cart
from .permissions import IsManager, IsDeliveryCrew, IsSuperUser, IsCustomer
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer


# MANAGER VIEWS - Handling Manager Group by the admin
@api_view(['POST', 'DELETE'])
@permission_classes([IsSuperUser])
def managers(request):
    username = request.data['username']
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name='Manager')
        if request.method =='POST':
            managers.user_set.add(user)
        if request.method =='DELETE':
            managers.user_set.remove(user)
        return Response({"mesage": "ok"})
    return Response({'message': "error"}, status.HTTP_400_BAD_REQUEST)



# CATEGORY VIEWS
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['title']
    
    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsSuperUser]
        return super(CategoriesView, self).get_permissions()
        

class SingleCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUser]



# MENU ITEM VIEWS
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'stock']
    filterset_fields = {'category': ['exact'], 
                        'price':['gte', 'lte']
                        }
    search_fields = ['title']

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsSuperUser | IsManager]
        return super(MenuItemsView, self).get_permissions()



class MenuItemsSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsSuperUser | IsManager]
        return super(MenuItemsSingleView, self).get_permissions()
    
    
# CART VIEWS
class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
        
    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsCustomer]
        return super(CartView, self).get_permissions()
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(CartView, self).form_valid(form)