from django.db import models


class Proxy(models.Model):
    ip = models.CharField(max_length=255)
    port = models.CharField(max_length=20)
    protocols = models.JSONField(default=list)
    country = models.CharField(max_length=100)
    uptime = models.CharField(max_length=255)
