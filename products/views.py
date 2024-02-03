from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    query = request.GET.get('q')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'products/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'query': query  
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    reviews = product.reviews.all()
    return render(request, 'products/detail.html', {'product': product, 'reviews': reviews})
