from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def order_tracking_page(request):
    return render(request, "index.html")
