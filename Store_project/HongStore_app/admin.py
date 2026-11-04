from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Computer)
admin.site.register(models.Keyboard)
admin.site.register(models.Mouse)
admin.site.register(models.OrderLaptop)
admin.site.register(models.OrderKeyboard)
admin.site.register(models.OrderMouse)
admin.site.register(models.Customer)