from django.db import models

# Create your models here.

class Welcome(models.Model):
    message = models.TextField()