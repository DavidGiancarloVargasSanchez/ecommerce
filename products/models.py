from django.db import models
from django.core.validators import MaxValueValidator
from users.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category', null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=600, null=True)
    image = models.ImageField(upload_to='products', null=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5)])
    comment = models.TextField(max_length=200, default='')
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.date_posted


