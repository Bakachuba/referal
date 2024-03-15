from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from service.models import ReferralCode
from service.serializers import CodeSerializer


def index(request):
    return render(request, 'service/index.html')

#
# class CodeViewSet(generics.ListCreateAPIView, generics.DestroyAPIView):
#     permission_classes = [IsAuthenticated, IsAdminUser]
#     queryset = ReferralCode.objects.filter(status=True)
#     serializer_class = CodeSerializer
