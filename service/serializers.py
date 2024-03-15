from rest_framework import serializers

from service.models import ReferralCode


class CodeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # Устанавливаем текущего пользователя по умолчанию

    class Meta:
        model = ReferralCode
        fields = ['code', 'expiration_date', 'status', 'user', 'id']
