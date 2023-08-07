from django.contrib import admin

# Register your models here.
from .models import Category,Product

class Catogeryadmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,Catogeryadmin)
class Productadmin(admin.ModelAdmin):
    list_display=['name','price','stock','available','created','updated']
    list_editable=['price','available','stock']
    prepopulated_fields={'slug':('name',)}
    list_per_page=20
admin.site.register(Product,Productadmin)

