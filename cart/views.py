from django.shortcuts import render, redirect
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def _cart_id(request):
    cart= request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart
    




def add_cart(request, product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart= Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id(request))
    cart.save()
    try:
        cart_item=CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
        
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(cart=cart, product=product, quantity = 1)
        cart_item.save()
    return redirect('cart')


def cart(request, total=0, cart_items=None, quantity=0):
    sub_total=0
    tax=0
    try:
    
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax= (total * 2)/ 100
        sub_total= total + tax
        
    except ObjectDoesNotExist:
        pass
    
    context={'total': total, 'quantity': quantity, 'cart_items': cart_items, 'tax': tax, 'sub_total': sub_total}
    return render(request, 'store/cart.html', context)



def remove_cart(request, product_id):
    product=Product.objects.get(id=product_id)
    cart=Cart.objects.get(cart_id=_cart_id(request))
    cart_item=CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('cart')

def minus_cart(request, product_id):
    product=Product.objects.get(id=product_id)
    cart=Cart.objects.get(cart_id=_cart_id(request))
    cart_items=CartItem.objects.get(cart=cart, product=product)
    if cart_items.quantity > 1:
        cart_items.quantity -= 1
        cart_items.save()
    else:
        cart_items.delete()
    return redirect('cart')
        
    