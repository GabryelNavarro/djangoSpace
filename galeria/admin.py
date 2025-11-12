from django.contrib import admin
from galeria.models import Fotografia
from rangefilter.filters import DateRangeFilter


class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda","publicado","data_fotografia","categoria")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_per_page = 5
    list_filter =("categoria","publicado","categoria",("data_fotografia",DateRangeFilter),)
    

  
   

admin.site.register(Fotografia,ListandoFotografias)
