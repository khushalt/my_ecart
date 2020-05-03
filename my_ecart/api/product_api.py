from rest_framework.response import Response
from ..models import Product
from ..serilizer import ProductSerilizer
from rest_framework.views import APIView
from django.http import HttpResponse


class ProductList(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serilizer = ProductSerilizer(products, many=True)
        return Response(serilizer.data)

    def post(self, request, format=None):
        serilizer = ProductSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors)


class ProductDetail(APIView):

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Exception as e:
            return Response({"error": "Given question object not found."})

    def get(self, request, id=None):
        serilizer = ProductSerilizer(self.get_object(id))
        return Response(serilizer.data)

    def put(self, request, id=None):
        serializer = ProductSerilizer(self.get_object(id), request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros)

    def delete(self, request, id=None):
        self.get_object(id).delete()
        return HttpResponse(status=204)
