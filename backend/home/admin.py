from django.contrib import admin
from home.models import BookRide, BookRideAdmin, Contact, ContactAdmin

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(BookRide, BookRideAdmin)
