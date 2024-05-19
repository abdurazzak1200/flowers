from django.db import models
from django.contrib.auth.models import User

class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    method = models.CharField(max_length=100, verbose_name='Способ оплаты')


