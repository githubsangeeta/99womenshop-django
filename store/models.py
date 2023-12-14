from django.db import models
from catagory.models import catagory
from catagory.models import reverse
from django.urls import reverse 


# Create your models here.
class product(models.Model):
    product_name =models.CharField(max_length=200, unique=True)
    slug         =models.SlugField(max_length=200, unique=True)
    description  =models.TextField(max_length=500, blank=True)
    price        =models.IntegerField()
    images       =models.ImageField(upload_to='photos/products')
    stock        =models.ImageField()
    is_available =models.BooleanField(default=True)
    catagory     =models.ForeignKey(catagory, on_delete=models.CASCADE)
    created_date =models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detail',args=[self.catagory.slug, self.slug])
    
    def __str__(self):
        return self.product_name  
    