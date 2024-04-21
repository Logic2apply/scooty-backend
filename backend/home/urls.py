from django.urls import include, path
from home import views
urlpatterns = [
    path('', views.index, name='index'),
]