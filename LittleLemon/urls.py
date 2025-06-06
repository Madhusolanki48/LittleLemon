from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('say_hello/', views.say_hello, name='say_hello'),
    path('display_date/', views.display_date, name='display_date'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:menu_id>/', views.menu_by_id, name='menu_by_id'),


    # Class-Based Views (CBVs)
    path('menus/', views.MenuListView.as_view(), name='menu_list'),
    path('myview/', views.MyView.as_view(), name='my_view'),

    # Request and Response
    path('demo/', views.index, name='index'), 

    # Parameters
    path('getuser/<str:name>/<int:id>/', views.pathview, name='pathview'),   #Path parameters
    path('getuser/', views.qryview, name='qryview'),     #Query parameters

    # To handle form submission
    path('showform/', views.showform, name='showform'),
    path('getform/', views.getform, name='getform'),
 
    # Mapping URLs with params
    path('drinks/<str:drink_name>', views.drinks, name='drink_name'),

    # Regular Expressions or RegEx
    # path('menu_item/10',views.display_menu_item),
    re_path(r'^menu_item/([0-9]{2})/$',views.display_menu_item),
]
