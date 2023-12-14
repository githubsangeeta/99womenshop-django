from django.db import models
from django.urls import reverse

# Create your models here.
class catagory(models.Model):
    catagory_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=False)
    cat_image = models.ImageField(upload_to='photos/catagories',blank=True)
    
    class Meta:
        verbose_name = 'catagory'
        verbose_name_plural = 'catagories'
       #to display the product list by catagory slug in all catagory near in store
    def get_url(self):
            return reverse('products_by_catagory', args=[self.slug])
    
    def __str__(self):
        return self.catagory_name
