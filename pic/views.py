from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    if request.method=="POST":
        search=request.POST['search']
        images=Image.objects.filter(title__icontains=search)
        cats=Category.objects.filter(title__icontains=search) 
        data={
            'cats':cats,
            'images':images,
        }
        return render(request,'index.html',data)
    else:
        cats=Category.objects.all()
        images=Image.objects.all()
        
        data={
              'images' : images,
              'cats':cats,
        
             }
        
    
    return render(request,'index.html',data)

   


def showpage(request,sss):
    
    cats=Category.objects.all()

    category=Category.objects.get(pk=sss)
    images=Image.objects.filter(cat=category)
    data={
        'images' : images,
        'cats':cats
        
        }
        
    
    return render(request,'index.html',data)
