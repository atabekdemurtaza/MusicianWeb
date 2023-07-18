from django.shortcuts import render, redirect
from .models import Product
from .models import Repair

from .forms import ProductForm
#from .forms import RepairForm


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES) 
        if form.is_valid():     # True
            form.save()
            """cd = form.cleaned_data
            Product.objects.create(
                title=cd['title'],
                image=cd['image'],
                description=cd['description'],
                price=cd['price'],
                author=cd['author'],
                condition=cd['condition']
            )"""
        return redirect(to='sale')
    else:
        form = ProductForm()
    
    #print(ProductForm(request.POST).is_valid())
    context = {
        'form': form
    }
    return render(request, 'pages/create.html', context)


def sale(request):
    products = Product.objects.all()    # SELECT * FROM Product;
    context = {
        'products': products
    }
    return render(
        request,
        'pages/sale.html',
        context
    )


def sale_detail(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    
    #   product = get_object_or_404(Product, id=pk)
    context = {
        'product': product
    }
    return render(request, 'pages/sale_detail.html', context)


def repairs(request):
    repairs = Repair.objects.all()
    context = {
        'repairs': repairs
    }
    return render(request, 'pages/repairs.html', context)


#   *args, **kwargs
