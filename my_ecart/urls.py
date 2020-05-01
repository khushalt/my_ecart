from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.ProductList.as_view()),
    path('productcategories/', views.ProductCategoryList.as_view())
]