from django.urls import path
from . import views
from .api.product_api import ProductList, ProductDetail

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', ProductList.as_view()),
    path('products/<int:id>/', ProductDetail.as_view()),
    path('productcategories/', views.ProductCategoryList.as_view())
]