from django.contrib import admin

# Register your models here.

from .models import Photographer,Location,Image,Category

admin.site.register(Photographer)
admin.site.register(Location)
admin.site.register(Image)
admin.site.register(Category)

