from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_display_prise(self):
        return "{0:.2f}".format(self.price / 100)
