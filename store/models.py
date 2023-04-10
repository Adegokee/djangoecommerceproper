from django.db import models
from cartegory.models import Cartegory
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    stock=models.IntegerField()
    description=models.TextField()
    price=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    modify_date=models.DateTimeField(auto_now=True)
    is_available=models.BooleanField(default=True)
    images=models.ImageField(upload_to='photos/product')
    cartegory=models.ForeignKey(Cartegory, on_delete=models.CASCADE)
    
    
    def get_url(self):
        return reverse('product_details', args=[self.cartegory.slug, self.slug])
    
    
    def __str__(self):
        return self.product_name