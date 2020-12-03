from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
# Create your models here.


class DeviceQuerySet(models.QuerySet):
    pass


class DeviceManager(models.Manager):
    def get_queryset(self):
        return DeviceQuerySet(self.model, using=self._db)


class Device(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                         on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    hostname = models.TextField(null=True, blank=True)
    ipaddress = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = DeviceManager()

    def __str__(self):
        return str(self.hostname)[:50]

    class Meta:

        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
