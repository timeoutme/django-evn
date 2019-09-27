from django.db import models

# Create your models here.

class Toto(models.Model):
    items = models.CharField(max_length=100)
    achieve = models.BooleanField(default=False)

    def __str__(self):
        return self.items