from django.contrib import admin
from api.models import *
# Register your models here.



@admin.register(Post)
class PostModel(admin.ModelAdmin):
    list_filter = ['title', 'time']
    list_display = ['title', 'text','time']

