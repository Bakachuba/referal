from django.urls import path, include
from rest_framework import routers

from service.views import CodeViewSet

router = routers.SimpleRouter()
router.register(r'code', CodeViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls
