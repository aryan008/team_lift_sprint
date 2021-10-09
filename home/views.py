from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "home/index.html")


def contact(request):
    return render(request, "home/contact.html")


def faq(request):
    return render(request, "home/faq.html")


def shipping_info(request):
    return render(request, "home/shipping_info.html")
