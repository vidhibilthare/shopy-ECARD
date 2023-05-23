from django.shortcuts import render,redirect
from .models import *
from django.views import View

# def home(request):
#  return render(request, 'app/home.html')
class ProductView(View):
    def get(Self, request):
     topwears = Product.objects.filter(category='TW')
     bottomwears = Product.objects.filter(category='BW')
     electronics = Product.objects.filter(category='E')
     accessories = Product.objects.filter(category='A')
     return render(request,'app/home.html',
                   {'topwears': topwears, 'bottomwears' : bottomwears, 'electronics': electronics, 'accessories' : accessories})

def product_detail(request):
 products = Product.objects.all()
 context = { 'products':products}
 return render(request, 'app/productdetail.html',context)

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')


 


 
 
 
 