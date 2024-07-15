from django.shortcuts import render
from .models import products
# Create your views here.

def product_list(request):
    products = product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'e_commerce/product_list.html', context)
