from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=25)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()