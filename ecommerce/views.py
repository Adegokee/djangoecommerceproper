from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.db.models import Q



def home(request):
  
    products=Product.objects.filter(is_available=True)
    product_count=products.count()
    context={'products': products, 'product_count': product_count}
    return render(request, 'home.html', context)


