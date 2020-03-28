
from django.contrib import admin
from . models import Products,Contact,Orders,Order_update

admin.site.register(Products)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(Order_update)