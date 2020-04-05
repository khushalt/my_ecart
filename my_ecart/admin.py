from django.contrib import admin
from .models import CouponType, User, Product, ProductCategory

# Register your models here.

admin.site.register(CouponType)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(ProductCategory)

