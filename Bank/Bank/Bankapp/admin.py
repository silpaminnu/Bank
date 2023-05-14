


from django.contrib import admin

# Register your models here.
from.models import Person,District,Branches
class personadmin(admin.ModelAdmin):
    list_display=['name','District']
    admin.site.register(Person)
admin.site.register(District)
admin.site.register(Branches)