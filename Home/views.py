from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request,'Home/index.html')
# return HttpResponse("This is home page")


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')

def review(request):
    return render(request,'review.html')

def cart(request):
    return render(request,'cart.html' )

def product(request):
    return render(request,'product.html' )