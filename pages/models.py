from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
