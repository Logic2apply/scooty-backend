from django.urls import include, path
from home import views
urlpatterns = [
    path("", views.index, name="index"),
    path("vehicle/", views.vehicle, name="vehicle"),
    path("contact/", views.contact, name="contact"),
]
