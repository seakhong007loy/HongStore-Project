from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Computer(models.Model):
    name = models.CharField(max_length=2200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    photo_first = models.ImageField(upload_to='photo/', default=None)
    photo_second = models.ImageField(upload_to='photo/', default=None)
    detail = models.TextField(default=None)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Keyboard(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    photo_first = models.ImageField(upload_to='photo/', default=None)
    photo_second = models.ImageField(upload_to='photo/', default=None)
    detail = models.TextField(default=None)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Mouse(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    photo_first = models.ImageField(upload_to='photo/', default=None)
    photo_second = models.ImageField(upload_to='photo/', default=None)
    detail = models.TextField(default=None)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OrderLaptop(models.Model):
    STATUS = (
        ('J&T Express', 'J&T Express'),
        ('Vireak Buntham Express', 'Vireak Buntham Express'),
        ('Saly VIP', 'Saly VIP'),
    )

    laptop = models.ForeignKey(Computer, null=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    delivery = models.CharField(max_length=200, choices=STATUS)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    date_create = models.DateTimeField(auto_now_add=True)


class OrderKeyboard(models.Model):
    STATUS = (
        ('J&T Express', 'J&T Express'),
        ('Vireak Buntham Express', 'Vireak Buntham Express'),
        ('Saly VIP', 'Saly VIP'),
    )

    keyboard = models.ForeignKey(Keyboard, null=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    delivery = models.CharField(max_length=200, choices=STATUS)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    date_create = models.DateTimeField(auto_now_add=True)

class OrderMouse(models.Model):
    STATUS = (
        ('J&T Express', 'J&T Express'),
        ('Vireak Buntham Express', 'Vireak Buntham Express'),
        ('Saly VIP', 'Saly VIP'),
    )

    mouse = models.ForeignKey(Mouse, null=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    delivery  = models.CharField(max_length=200, choices=STATUS)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    date_create = models.DateTimeField(auto_now_add=True)

