from django.urls import path, include

from service import views

urlpatterns = [
    path('', views.index, name='index'),
]
