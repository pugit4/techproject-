from django.contrib import admin
from .models import members

# Register your models here.
class Memberadmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "position", "employee_id")
    
    
admin.site.register(members, Memberadmin)

