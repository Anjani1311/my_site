from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(User)
admin.site.register(Contact)


@admin.register(News)
class News_details(admin.ModelAdmin):
    list_display = ['Heading', 'category', 'subcategory',
                    'description', 'publish_date', 'image']

