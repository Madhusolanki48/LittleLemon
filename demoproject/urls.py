from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LittleLemon.urls')), 

]
# handle errors demo
# handler404='LittleLemon.views.handler404'
