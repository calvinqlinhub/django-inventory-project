from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})

from .forms import ProductForm
from django.shortcuts import redirect


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "product_form.html", {"form": form})

def product_edit(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)

    return render(request, "product_form.html", {"form": form})

def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect("product_list")