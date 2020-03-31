from django.contrib import admin
from .models import Todo # added


class TodoAdmin(admin.ModelAdmin): # added
    list_display = ('title', 'description', 'completed')



# Register your models here.
admin.site.register(Todo, TodoAdmin) # added

