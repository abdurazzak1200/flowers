from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='ФИО', max_length=200)
    birth_day = models.DateTimeField(verbose_name='Дата рождения', blank=True, null=True)
    city = models.CharField(verbose_name='Город', max_length=200, blank=True, null=True)
    adres = models.CharField(verbose_name='Адрес', max_length=200, blank=True, null=True)
    phone = models.CharField(verbose_name='Номер телефона', max_length=200, blank=True, null=True)
    email = models.CharField(verbose_name='E-mail', max_length=200, blank=True, null=True)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user}'s profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




