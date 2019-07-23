from django.contrib import admin
from .models import Adnow

# Register your models here.
@admin.register(Adnow)
class AdnowAdmin(admin.ModelAdmin):
    lst_display = ['Ctry_name','Methhodology','Plat_Method']
