from django.urls import path

from .views import CategoriesView, SingleCategoryView, MenuItemsView, MenuItemsSingleView

urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='list-categories'),
    path('categories/<int:pk>/', SingleCategoryView.as_view(), name='single-category'),
    path('menu-items/', MenuItemsView.as_view(), name='list-menu-items'),
    path('menu-items/<int:pk>/', MenuItemsSingleView.as_view(), name='single-menu-item'),
]