from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.http import StreamingHttpResponse
from .models import *
import json
from django.template.loader import get_template
from django.http import HttpResponseRedirect 
from .forms import NameForm

def ordering(request):
    return render(request, 'my_app/ordering.html')






def buy(request): 
    if request.method == 'POST': 
        form = NameForm(request.POST) 
        if form.is_valid():
            #print(form.cleaned_data)
            #feed = NameForm(
                #email = form.cleaned_data['email'],
                #phone_number = form.cleaned_data['phone_number'],
            #)
            form.save()
            return redirect ('ordering')
    else:
        form = NameForm() 
    return render(request, 'my_app/buy.html', context={'form': form})


#def buy(request): 
    if request.method == 'POST': 
        form = NameForm(request.POST) 
        if form.is_valid():
            return HttpResponseRedirect('/ordering/')
     
    else:
        form = NameForm() 
        return render(request, 'my_app/buy.html', {'form': form})


#def buy(request):
    #return render(request, 'my_app/buy.html')



def main(request):
    return render(request, 'my_app/main.html')




def base(request):
    return render(request, 'my_app/base.html')




def index(request):
    categories = Category.objects.all()
    return render(request, 'my_app/index.html',{'categories':categories})




def get_products(request, category_id=None):
    categories = Category.objects.all()
    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, 'my_app/products.html', context)




def get_product(request: HttpRequest, id: int):
    product = get_object_or_404(Product, id=id)
    context = {'product': product}
    return render(request, 'my_app/product.html', context)


