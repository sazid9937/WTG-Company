from unicodedata import category
from django.db import models

# Create your models here.


class category_p(models.Model):
    category_id=models.IntegerField()
    name=models.CharField(max_length=50)
    
class surfaces(models.Model):    
    surface_id=models.IntegerField()
    name=models.CharField(max_length=150)
    glass_or_aluminium=models.CharField(max_length=50)
    
    
class product(models.Model):    
    product_id=models.BigIntegerField()
    model=models.CharField(max_length=200)
    product_category=models.ForeignKey(category_p,on_delete=models.CASCADE)
    product_surface = models.ForeignKey(surfaces, on_delete=models.CASCADE)
    size=models.CharField( max_length=50)
    tone_of_color=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    opacity=models.CharField(max_length=50)
    deleted=models.IntegerField()
    image=models.ImageField(upload_to='media/product', height_field=None, width_field=None, max_length=None)
    