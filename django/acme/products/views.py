from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Category
# from django.template.loader import get_template

def testController(request):
    return HttpResponse("Test")

def listProducts(request):
    try:
        categories = Category.objects.all().order_by('name')
        # ou product = Product.objects.get(pk=id)
    except:
        return redirect('noProduct')
    else:
        context = {'categories': categories}
        return render(request, 'listProducts.html', context)

def showProduct(request, id):
    try:
        product = Product.objects.get(id=id)
        # ou product = Product.objects.get(pk=id)
    except:
        return redirect('noProduct')
    else:
        context = {'product': product }
        return render(request, 'showProduct.html', context)

def noProduct(request):
    # return HttpResponse(f"Produit introuvable")
    return render(request, 'noProduct.html')