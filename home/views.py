from django.shortcuts import render, HttpResponse 
from home.models import contact


def index(request):
   return render(request, 'index.html')
   # return HttpResponse('HOMEPAGE')

def about(request):
   return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')  

def contact(request):
         


     return render(request, 'contact.html')
    