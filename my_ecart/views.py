from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serilizer import ProductSerilizer
from rest_framework.views import APIView


# Create your views here.


def home(request):
    return render(request, 'home.html')


class ProductList(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serilizer = ProductSerilizer(products, many=True)
        return Response(serilizer.data)


