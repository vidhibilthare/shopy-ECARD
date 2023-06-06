from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.db.models import Q
from django.http import JsonResponse
from django.contrib import messages
from .forms import CustomerRegistrationForm, CustomerProfileForm
# from django.contrib.auth.decorators import login_required


class ProductView(View):
    def get(Self, request):
        topwears = Product.objects.filter(category="TW")
        bottomwears = Product.objects.filter(category="BW")
        electronics = Product.objects.filter(category="E")
        accessories = Product.objects.filter(category="A")
        return render(
            request,
            "app/home.html",
            {
                "topwears": topwears,
                "bottomwears": bottomwears,
                "electronics": electronics,
                "accessories": accessories,
            },
        )


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)
            ).exists()
            return render(
                request,
                "app/productdetail.html",
                {"product": product, "item_already_in_cart": item_already_in_cart},
            )
        else:
            return render(
                request,
                "app/productdetail.html",
                {"product": product, "item_already_in_cart": item_already_in_cart},
            )


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get("prod_id")
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect("/cart")


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = p.quantity * p.product.discount_price
                amount += tempamount
                total_amount = amount + shipping_amount
            return render(
                request,
                "app/addtocart.html",
                {"carts": cart, "total_amount": total_amount, "amount": amount},
            )
        else:
            return render(request, "app/emptycart.html")


def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET["prod_id"]
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = p.quantity * p.product.discount_price
            amount += tempamount

        data = {
            "quantity": c.quantity,
            "amount": amount,
            "totalamount": amount + shipping_amount,
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET["prod_id"]
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = p.quantity * p.product.discount_price
            amount += tempamount

        data = {
            "quantity": c.quantity,
            "amount": amount,
            "totalamount": amount + shipping_amount,
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET["prod_id"]
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = p.quantity * p.product.discount_price
            amount += tempamount

        data = {"amount": amount, "totalamount": amount + shipping_amount}
        return JsonResponse(data)


def buy_now(request):
    return render(request, "app/buynow.html")


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, "app/address.html", {"add": add, "active": "btn-primary"})


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(
            request, "app/profile.html", {"form": form, "active": "btn-primary"}
        )

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data["name"]
            locality = form.cleaned_data["locality"]
            city = form.cleaned_data["city"]
            state = form.cleaned_data["state"]
            zipcode = form.cleaned_data["zipcode"]
            reg = Customer(
                user=usr,
                name=name,
                locality=locality,
                city=city,
                state=state,
                zipcode=zipcode,
            )
            reg.save()
            messages.success(request, "Congratulation!! Profile Updated Succesfully")
        return render(
            request, "app/profile.html", {"form": form, "active": "btn-primary"}
        )


def orders(request):
    return render(request, "app/orders.html")


def change_password(request):
    return render(request, "app/changepassword.html")


def mobile(request):
    return render(request, "app/mobile.html")


def login(request):
    return render(request, "app/login.html")


def customerregistration(request):
    return render(request, "app/customerregistration.html")

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulation!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})


def checkout(request):
    return render(request, "app/checkout.html")
