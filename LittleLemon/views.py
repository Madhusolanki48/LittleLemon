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

# Request and Response Objects
def index(request):
    # Getting the request path and method
    path = request.path
    method = request.method
    # Creating the content to display
    content = '''
    <center><h2>Testing Django Request Response Objects</h2>
    <p>Request path : " {}</p>
    <p>Request Method :{}</p></center>
    '''.format(path, method)
    # Returning an HttpResponse with the content
    return HttpResponse(content)


# Parameters 

def pathview(request, name, id):        #path parameter
    return HttpResponse(f"Name: {name} UserID: {id}")

def qryview(request):                  #Query parameter
    name = request.GET.get('name')
    user_id = request.GET.get('id')
    return HttpResponse(f"Name: {name} UserID: {user_id}")

#showform and getform functions
# This view renders the form
def showform(request):
    return render(request, "form.html")

# This view handles the form submission
def getform(request): 
    if request.method == "POST": 
        id = request.POST['id'] 
        name = request.POST['name'] 
        return HttpResponse("Name:{} UserID:{}".format(name, id))
    else:
        return HttpResponse("Please submit the form via POST.")
    

# Mapping URLs with Params
def drinks(request, drink_name):
    drink = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment',
        'cola': 'type of soda',
    }
    choice_of_drink = drink.get(drink_name, 'Unknown drink')
    return HttpResponse(f"<h2>{drink_name}</h2>{choice_of_drink}")

# Regular Expression
def display_menu_item(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    return render(request, 'menu_items.html', {'menu_item': menu_item})


