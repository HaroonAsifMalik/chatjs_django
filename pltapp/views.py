from django.shortcuts import render, redirect , get_list_or_404
from . models import Product
from . forms import ProductForm

# Create your views here.

def index(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    else:
        form = ProductForm()        

    context = {
        "products": products,
        "form": form
    }

    return render(request, 'pltapp/index.html', context)

#update data 

# def  updated(request , product_id):

#     product = get_list_or_404(Product , pk=product_id)

#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ProductForm(instance=product)

#     context = {
#         'form': form,
#         'product': product
#     }

#     return render(request, 'pltapp/update.html', context)

def  update_page(request , product_id):

    product = get_list_or_404(Product , pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product
    }

    return render(request, 'pltapp/update.html', context)
