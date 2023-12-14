from django.shortcuts import render, get_object_or_404
from .models import product  
from catagory.models import catagory

# Create your view here
def store(request, catagory_slug=None):
    catagories = None
    products = None
    
    if catagory_slug !=None:
        catagories = get_object_or_404(catagory, slug=catagory_slug )
        products = product.objects.filter(catagory=catagories, is_available=True)
        product_count = products.count()
    else:
        products = product.objects.all().filter(is_available=True)
        product_count = products.count()
    
    context = {
        'products': products,
        'product_count':product_count,
    }
    
    return render(request, 'store/store.html', context)  # Pass the context to the template

#to create product details page
def product_detail(request, catagory_slug, product_slug):
    try:
        single_product = product.objects.get(catagory__slug=catagory_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)
    

