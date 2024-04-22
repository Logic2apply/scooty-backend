from os import name
from django.db import models
from django.contrib import admin

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    fname = models.TextField(max_length=100, default=True, null=False)
    lname = models.TextField(max_length=100, default=True, null=False)
    email = models.EmailField(max_length=100, default=True, null=False)
    message = models.TextField(max_length=1000, default=True, null=False)

    def __str__(self):
        return self.fname + " " + self.lname + " " + self.email + " " + self.message
    
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "fname",
        "lname",
        "email",
        "message",
    ]


class BookRide(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.TextField(max_length=100, default="", null=False)
    email = models.EmailField(max_length=100, default="", null=False)
    contact = models.IntegerField(default=0, null=False)
    other = models.TextField(max_length=100, default='')
    biketype = models.TextField(max_length=250, default="", null=False)
    datetimef = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.email + " " + str(self.contact) + " " + self.other + " " + self.biketype + " " + str(self.datetimef)

class BookRideAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "contact",
        "other",
        "biketype",
        "datetimef",
    ]

class EmailSubscribe(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    email = models.EmailField(max_length=100, default="", null=False, unique=True)

    def __str__(self):
        return self.email