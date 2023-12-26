from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product_id=product.id, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    
    # Update the cart
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'update': True
        })
    
    return render(request, 'cart/details.html', {'cart': cart})

@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        update_quantity = cd['update']
        quantity = cd['quantity']
        if update_quantity:
            # This ensures that the quantity is set to the new value
            cart.add(product_id=product.id, quantity=quantity, update_quantity=True)
        else:
            # Add additional quantity to what's already in the cart
            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)
        return redirect('cart:cart_detail')

    return render(request, 'cart/details.html', {'cart': cart})