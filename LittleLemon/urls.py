from django.urls import path
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
]
