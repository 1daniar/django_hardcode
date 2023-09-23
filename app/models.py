from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    owners = models.ManyToManyField(User, related_name='product_list')
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    product = models.ForeignKey(Product, related_name='lesson_list', on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=50)
    link = models.CharField('Link', max_length=200)
    seconds = models.IntegerField()
    user_seconds = models.IntegerField()
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return self.name