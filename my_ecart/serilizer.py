from  rest_framework import serializers
from .models import Product


class ProductSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'category_id', 'rate', 'description')
