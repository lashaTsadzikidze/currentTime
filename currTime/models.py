from django.db import models

# Create your models here.
class DateTime(models.Model):
    datetime = models.DateTimeField()

    def __str__(self):
        return self.datetime