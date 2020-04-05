from django.contrib import admin
from .models import CouponType
from .models import User

# Register your models here.

admin.site.register(CouponType)
admin.site.register(User)