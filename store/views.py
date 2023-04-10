from django.shortcuts import render, get_object_or_404
from .models import Product
from cartegory.models import Cartegory
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.


def store(request, cartegory_slug=None):
    cartegories=None
    products=None
    if cartegory_slug is not None:
        cartegories=get_object_or_404(Cartegory, slug=cartegory_slug)
        products=Product.objects.filter(cartegory=cartegories, is_available=True)
        paginator= Paginator(products, 1)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        product_count=products.count()
            
    else:
        products=Product.objects.filter(is_available=True).order_by('id')
        paginator= Paginator(products, 3)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        product_count=products.count()
    context={'products': paged_products, 'product_count': product_count}
    return render(request, 'store/store.html', context)


def product_details(request, product_slug, cartegory_slug):
    try:
        single_product=Product.objects.get(cartegory__slug=cartegory_slug, slug=product_slug)
        in_cart=CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    context={'single_product': single_product, 'in_cart': in_cart}
    return render(request, 'store/product_details.html', context)



def search(request):
    # products=None
    # product_count=None
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products=Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword)|Q(product_name__icontains=keyword))
            product_count=products.count()
    context={'products': products, 'product_count': product_count}
    return render(request, 'store/store.html', context)







