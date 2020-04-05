from django.db import models


# Create your models here.


class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=30)
    alternate_phone = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    category_id = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING)
    rate = models.FloatField(max_length=20)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CartOrder(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=30)
    order_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    total_actual_amount = models.FloatField(max_length=20)
    total_discounted_amount = models.FloatField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    order_id = models.ForeignKey(CartOrder, on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.FloatField(max_length=20)
    amount = models.FloatField(max_length=20)


class CouponType(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    amount = models.FloatField(max_length=20)
    description = models.CharField(max_length=100)


class Coupon(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    type_id = models.ForeignKey(CouponType, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Address(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


class CartOrderCoupen:
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    order_id = models.ForeignKey(CartOrder, on_delete=models.DO_NOTHING)
    coupon_id = models.ForeignKey(Coupon, on_delete=models.DO_NOTHING)