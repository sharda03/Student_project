from django.contrib import admin
from .models import CustomeModel
# Register your models here.

class CustomAdmin(admin.ModelAdmin):
    list_display=['username','user_type']

admin.site.register(CustomeModel,CustomAdmin,)