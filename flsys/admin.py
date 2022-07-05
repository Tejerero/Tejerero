from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Registration,CookingClass,Schedule,CheckoutInfo,Email,Rating ])
