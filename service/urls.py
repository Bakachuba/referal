from django.urls import path, include, re_path

from service import views

# from service.views import CodeViewSet

urlpatterns = [
    # path('api/', CodeViewSet.as_view(), name='CodeViewSet'),

    path('', views.index, name='index')

]
