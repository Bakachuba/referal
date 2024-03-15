from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ReferralCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True)
    expiration_date = models.DateTimeField()
    status = models.BooleanField(default=True)

    def is_expired(self):
        return self.expiration_date < timezone.now()

    def save(self, *args, **kwargs):
        # Проверка срока годности кода
        if self.is_expired():
            self.status = False
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Referral Code'
        verbose_name_plural = 'Referral Codes'


class Referral(models.Model):
    creator = models.ForeignKey(User, related_name='referrals_given', on_delete=models.CASCADE)
    referal = models.OneToOneField(User, related_name='referrer', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    referral_code = models.ForeignKey(ReferralCode, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, unique=True)

    def __str__(self):
        return self.user.username
