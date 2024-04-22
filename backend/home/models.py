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
