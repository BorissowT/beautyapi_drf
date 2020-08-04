from django.db import models
from django.contrib.auth.models import User

import datetime


class ProductSets(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()
    weight = models.IntegerField()


class Recipient(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, default='None')


class Order(models.Model):
    order_created_datetime = models.DateField(default=datetime.date.today)
    delivery_datetime = models.DateField(default=datetime.date.today() + datetime.timedelta(days=3))
    delivery_address = models.CharField(max_length=150)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, related_name='myorders')
    product_set = models.ForeignKey(ProductSets, on_delete=models.CASCADE, related_name='orders')
    choices = [
        ("CREATED", "created"),
        ("DELIVERED", "delivered"),
        ("PROCESSED", "processed"),
        ("CANCELLED", "cancelled")
    ]
    status = models.CharField(max_length=9, default="CREATED", choices=choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')