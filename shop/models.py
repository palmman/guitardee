from django.db import models
from datetime import datetime

# Create your models here.

class Shop(models.Model):

    categories_choice =(
        ('Guitar', 'Guitar'),
        ('Bass', 'Bass'),
    )

    product = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    categories = models.CharField(choices=categories_choice, max_length=250)
    color = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)
    product_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    product_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    product_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    product_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.brand

