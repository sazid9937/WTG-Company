from pickle import TRUE
from django.db import models
# from sqlalchemy import true

# Create your models here.


class category_p(models.Model):
    category_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    is_active=models.BooleanField(default='0')
    category_image=models.ImageField(upload_to='media/category', height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.name
    
class surfaces(models.Model):    
    surface_id=models.AutoField(primary_key=True)
    category_surface=models.ForeignKey(category_p, on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    surface_image=models.ImageField(upload_to='media/surface', height_field=None, width_field=None, max_length=None)
    is_active=models.BooleanField(default='0')
    
    def __str__(self):
        return self.name
    
    
class product_s(models.Model):    
    product_id=models.AutoField(primary_key=True)
    model=models.CharField(max_length=200)
    product_category=models.ForeignKey(category_p,on_delete=models.CASCADE)
    product_surface = models.ForeignKey(surfaces, on_delete=models.CASCADE)
    size=models.CharField( max_length=50)
    standard_thinckness=models.CharField( max_length=150)
    finish=models.CharField( max_length=150)
    deleted=models.IntegerField(default='0')
    image=models.ImageField(upload_to='media/product', height_field=None, width_field=None, max_length=None)
    is_active=models.BooleanField(default='0')
    
    def __str__(self):
        return self.model
    