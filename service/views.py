from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from service.models import ReferralCode
from service.permissions import IsOwner
from service.serializers import CodeSerializer


class CodeViewSet(ModelViewSet):
    serializer_class = CodeSerializer
    permission_classes = [IsOwner]
    queryset = ReferralCode.objects.none()

    def get_queryset(self):
        # Получаем только объекты ReferralCode, связанные с текущим пользователем
        return ReferralCode.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Проверяем, существует ли объект ReferralCode для текущего пользователя
        existing_referral_code = ReferralCode.objects.filter(user=self.request.user).first()
        if existing_referral_code:
            # Если объект уже существует, выбрасываем ошибку
            raise ValidationError("ReferralCode already exists for this user.")
        else:
            # Если объект не существует, сохраняем новый объект ReferralCode
            serializer.save(user=self.request.user)
