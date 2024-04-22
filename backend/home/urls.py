from django.urls import include, path
from home import views
urlpatterns = [
    path("", views.index, name="index"),
    path("vehicle/", views.vehicle, name="vehicle"),
    path("contact/", views.contact, name="contact"),
    path("book-test-ride/", views.bookTestRide, name="bookTestRide"),
    # Bikes
    path("450s", views.b450s, name="450s"),
    path("450x/", views.b450x, name="450x"),
    path("aurali/", views.baurali, name="aurali"),
    path("ezgo/", views.bezgo, name="ezgo"),
    path("falcon/", views.bfalcon, name="falcon"),
    path("kriti/", views.bkriti, name="kriti"),
    path("lithinoli/", views.blithinoli, name="lithinoli"),
    path("loev/", views.bloev, name="loev"),
    path("minilithino/", views.bminilithino, name="minilithino"),
    path("one/", views.bone, name="one"),
    path("roma/", views.broma, name="roma"),
    path("storie/", views.bstorie, name="storie"),
    path("stormzx/", views.bstormzx, name="stormzx"),
]
