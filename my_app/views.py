from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests

# Create your views here.

def home(request):
    return render(request, 'my_app/base.html')


def new_search(request):
    if request.POST.get('search'):
        search = request.POST['search']
        front_end = {
            'search': search
        }
        return render(request, 'my_app/new_search.html', front_end)
    return redirect('home', permanent=True)
