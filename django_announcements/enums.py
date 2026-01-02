from django.db import models

class Category(models.TextChoices):
    INF = 'inf', 'information'
    WRN = 'wrn', 'warning'
    CRT = 'crt', 'critical'