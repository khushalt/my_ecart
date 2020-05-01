from rest_framework import serializers

from my_ecart.models import Coupon, Address, CartOrderCoupen
from .models import Product, User, ProductCategory, CartOrder, CartItem, CouponType


class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User


class ProductCategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory


class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product


class CartOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartOrder


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem


class CouponTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponType


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address


class CartOrderCoupenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartOrderCoupen
