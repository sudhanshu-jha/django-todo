from django.contrib import admin

# Register your models here.
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    # list_display = ('Serial', 'Title', 'Description')
    search_fields = ['Title']

    # fields = ['Serial','Title','Description']
    fieldsets = [
        ('Serial', {'fields': ['Serial']}),
        # (None,  {'fields': ['Serial']}),
        ('Title', {'fields': ['Title']}),
        ('Description', {'fields': ['Description']}),
    ]
    list_filter = ['Title']
    
# admin.site.register(Todo)
admin.site.register(Todo,TodoAdmin)
