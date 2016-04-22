from django.contrib import admin

from .models import RainDataStore
# Register your models here.


class RainstoreDetailAdmin(admin.ModelAdmin):
    list_display = ("County", 'Month','Rainfall_Amount')




admin.site.register(RainDataStore, RainstoreDetailAdmin)


