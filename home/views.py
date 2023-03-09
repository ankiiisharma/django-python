from django.shortcuts import render, HttpResponse 
from home.models import Contact
from django.contrib import messages



def index(request):
   return render(request, 'index.html')
   
def ffcometitive(request):
   return render(request, 'index.html')

def about(request):
   return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')  

def contact(request):
   if request.method == 'POST':
      name = request.POST['name']
      email = request.POST['email']
      phone = request.POST['phone']
      desc = request.POST['desc']
      

      contact = Contact(name=name, email=email, phone=phone, desc=desc)
      contact.save()
      
      messages.success(request, 'SUBMITTED!')

   return render(request, 'contact.html')
    