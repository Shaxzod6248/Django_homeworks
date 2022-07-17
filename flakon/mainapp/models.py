from django.db import models


class Flakon(models.Model):
    name = models.CharField(max_length=15)
    capacity = models.FloatField()
    image = models.ImageField(upload_to="flakon")

    def __str__(self):
        return self.name
