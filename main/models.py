from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()