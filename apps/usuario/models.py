from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Perfil(AbstractUser):
	foto = models.ImageField(upload_to="Perfil", null=True, blank=True)
	telefono = models.CharField(null=True, max_length=20)
