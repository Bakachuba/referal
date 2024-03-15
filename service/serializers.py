from rest_framework import serializers

from service.models import ReferralCode


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCode
        fields = '__all__'
