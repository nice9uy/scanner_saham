from django.contrib import admin

# Register your models here.
from .models import DbAllStocks

class ListDbAllStocks(admin.ModelAdmin):
    list_display = ('id',
                    'code' ,
                    'company_name',
                    'listing_board',
                    )
    
admin.site.register(DbAllStocks , ListDbAllStocks)