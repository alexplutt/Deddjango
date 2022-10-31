from django.db import models

class Acc(models.Model):
    name = models.CharField(max_length=20)