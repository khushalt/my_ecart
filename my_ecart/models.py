from django.db import models


# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email_id = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=30)
    alternate_phone = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    description = models.CharField(max_length=100)


class ProductCategory(models.Model):
    category_id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


class Product(models.Model):
    product_id = models.CharField(max_length=30, primary_key=True)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING)
    rate = models.FloatField(max_length=20)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


class CartOrder(models.Model):
    cart_id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    order_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    total_actual_amount = models.FloatField(max_length=20)
    total_discounted_amount = models.FloatField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


class CartItems(models.Model):
    cart_item_id = models.CharField(max_length=30, primary_key=True)
    order_id = models.ForeignKey(CartOrder, on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    qty = models.FloatField(max_length=20)
    amount = models.FloatField(max_length=20)







