from django.contrib import admin
from Regapp.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ['Modelo', 'Ano', 'Cor', 'Placa']


admin.site.register(Car, CarAdmin)
