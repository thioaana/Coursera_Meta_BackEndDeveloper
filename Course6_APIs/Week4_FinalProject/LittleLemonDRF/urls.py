from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (CategoriesView, SingleCategoryView,
                    MenuItemsView, MenuItemsSingleView,
                    CartView, managers)

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('categories/', CategoriesView.as_view(), name='list-categories'),
    path('categories/<int:pk>/', SingleCategoryView.as_view(), name='single-category'),
    path('menu-items/', MenuItemsView.as_view(), name='list-menu-items'),
    path('menu-items/<int:pk>/', MenuItemsSingleView.as_view(), name='single-menu-item'),
    path('carts/', CartView.as_view(), name='list-carts'),
    path('groups/manager/users/', managers),

]