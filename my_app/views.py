from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from .models import Search

BASE_URL = 'https://losangeles.craigslist.org/search/?query={}'
# Create your views here.


def home(request):
    return render(request, 'my_app/base.html')


def new_search(request):
    if request.POST.get('search'):
        search = request.POST['search']
        # Entry into Database
        Search.objects.check(search=search)
        final_url = BASE_URL.format(quote_plus(search))
        response = requests.get(final_url)
        data = response.text
        soup = BeautifulSoup(data, features='html.parser')
        post_listings = soup.find_all('li', attrs={'class': 'result-row'})
        final_postings = []
        for post in post_listings:
            post_title = post.find(class_='result-title').text
            post_url = post.find('a').get('href')
            post_price = 'N/A'
            post_image = ''
            if post.find(class_='result-image').get('data-ids'):
                img_list_str = post.find(class_='result-image').get('data-ids')
                img_id = img_list_str.split(',')[0].split(':')[1]
                post_image = 'https://images.craigslist.org/{}_300x300.jpg'.format(img_id)

            if post.find(class_='result-price'):
                post_price = post.find(class_='result-price').text
            final_postings.append((post_title, post_url, post_price, post_image))
        front_end = {
            'search': search,
            'postings': final_postings,
        }
        return render(request, 'my_app/new_search.html', front_end)
    return redirect('home', permanent=True)
