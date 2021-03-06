from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, ProductCategory
from .serilizer import ProductSerilizer, ProductCategorySerilizer
from rest_framework.views import APIView


# Create your views here.


def home(request):
    return render(request, 'home.html')


class ProductCategoryList(APIView):

    def get(self, request, format=None):
        products = ProductCategory.objects.all()
        serilizer = ProductCategorySerilizer(products, many=True)
        return Response(serilizer.data)
