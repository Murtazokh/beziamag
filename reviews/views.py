from django.shortcuts import redirect, get_object_or_404
from .forms import ReviewForm
from products.models import Product

def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.product_id = product_id
            new_review.author = request.user
            new_review.save()
            return redirect('products:product_detail', id=product_id, slug=product.slug)
    else:
        form = ReviewForm()
    return redirect('products:product_detail', id=product_id, slug=product.slug)