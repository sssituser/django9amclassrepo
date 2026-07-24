from django.shortcuts import render,get_object_or_404,redirect
from myapp.models import Product
from myapp.forms import ProductForm

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    return render(request,'myapp/contact.html')

def register(request):
   pform = ProductForm()
   if request.method=='POST':
       pform = ProductForm(request.POST)
       if pform.is_valid():
           pform.save(commit=True)
           return redirect('/products')
   return render(request,'myapp/register.html',{'form':pform})

def findproduct(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,'myapp/find.html',{'prod':product})

def editproduct(request,id):
    product = get_object_or_404(Product,id=id)
    pform = ProductForm(instance=product)
    if request.method=='POST':
        pform=ProductForm(request.POST,instance=product)
        if pform.is_valid():
            pform.save()
            return redirect('/products')  
    return render(request,'myapp/edit.html',{'form':pform})

def deleteproduct(request,id):
    product = get_object_or_404(Product,id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('/products')
    return render(request,'myapp/del.html')

def getproducts(request):
    products = Product.objects.all()
    return render(request,'myapp/products.html',{'prods':products})


