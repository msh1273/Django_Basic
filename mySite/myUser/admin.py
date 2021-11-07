from django.contrib import admin
from .models import Myuser
# Register your models here.


class MyuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(Myuser, MyuserAdmin)
