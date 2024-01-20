from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length= 200, null= False , blank=False)
    ava_count =models.IntegerField() 
    
    def __str__(self):
        return (f"{self.name}--- {self.ava_count}")