from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'store/homepage.html')


def product_list(request):
    return render(request, 'store/product_list.html')


