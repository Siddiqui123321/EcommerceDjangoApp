from django.contrib import admin

# Register your models here.
from eCommerceApp.models import  Contact, Product

admin.site.register(Contact)
admin.site.register(Product)