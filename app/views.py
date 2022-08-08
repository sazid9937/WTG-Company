import imp
from unicodedata import name
from django.shortcuts import render
from .models import category_p,surfaces
# Create your views here.

def home(request):
    data=category_p.objects.all()
    context={'data':data}
    return render(request,"index.html",context)
def glass_surface(request,id):
    print("id--",id)
    if id=='5':
        print("into the glass")
        surface_glass=surfaces.objects.filter(category_surface=id)
        context={'surface':surface_glass}
        return render(request,'glass.html',context)
    else:
        return render(request,'notfound.html')
    #print(surface,"gffgffg")
    # surface_glass=surfaces.objects.filter(category_surface=id)
    
def product(request):
    return render(request,"product.html")

def aboutus(request):
    return render(request,"aboutus.html")