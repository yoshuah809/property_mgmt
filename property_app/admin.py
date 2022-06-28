from django.contrib import admin

from property_app.models import Property, Company, Comment

# Register your models here.

admin.site.register(Property)
admin.site.register(Company)
admin.site.register(Comment)