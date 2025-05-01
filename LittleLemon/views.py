from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import Menu
from django.views import View
from django.views.generic import ListView


# Create your views here.

def home(request):
    return render(request, 'home.html')

def menu_by_id(request, menu_id):
    # menu = Menu.objects.get(pk=menu_id)
    menu = get_object_or_404(Menu, pk=menu_id)

    # return HttpResponse(f"{menu.menu_item}:Type of {menu.cuisine} cuisine")
    return render(request, 'menu_card.html', {'menu': menu})
 
#  MVT 
def say_hello(request):
    return HttpResponse("Welcome to Little Lemon Restaurant")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style="color: #F4CE14;"> This is Little Lemon again !</h1>"""
    return HttpResponse(text)


# Views Logic 
# Class-Based View (CBV) for displaying menus as a list

class MenuListView(ListView):
    model = Menu
    template_name = 'menu_list.html'
    context_object_name = 'menus'

# Class-Based View (CBV) for handling GET and POST requests
class MyView(View): 
    def get(self, request): 
        # Logic to process GET request
        return HttpResponse('Response to GET request')

    def post(self, request): 
        # Logic to process POST request
        return HttpResponse('Response to POST request')



