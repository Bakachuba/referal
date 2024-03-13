from django.db import models

class PromoCode(models.Model):
    code = models.CharField(max_length=20)
    exp_date = models.DateTimeField()
    status = models.BooleanField()

