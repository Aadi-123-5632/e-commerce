from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages
def index(request):
    context = {
        'variable':"this is sent"
    }
    return render(request , "index.html")
def main(request):
    return render(request , "index.html") 
def images(request):
    return render(request , "images.html") 
def about(request):
    return render(request , "about.html")  
def services(request):
    return render(request , "services.html") 
def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        Phone=request.POST.get('Phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name , email=email ,phone=Phone ,desc=desc)
        contact.save()
        messages.success(request,"Your message has been sent")
    return render(request , "contact.html") 
def vision(request):
    return render(request , "vision.html") 
def starter(request):
    return render(request , "starter.html") 
def roti(request):
    return render(request , "roti.html") 
def maincourse(request):
    return render(request , "maincourse.html") 
def booking(request):
    return render(request , "booking.html") 
def food(request):
    return render(request , "food.html") 
# Create your views here.
