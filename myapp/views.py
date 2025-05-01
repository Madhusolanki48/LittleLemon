from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404, HttpResponse
from .models import Product
from .forms import MyForm
from django.core.exceptions import PermissionDenied
from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import FieldDoesNotExist


def home(request):
    return HttpResponse('Hello World !')

# ERROR HANDLING

# 1.Handling Errors in Views (Http404)
def detail(request, id):
    try:
        # Trying to get the product by primary key (id)
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        # Raise Http404 if the product is not found
        raise Http404("Product does not exist")
    return HttpResponse(f"Product Found: {product.name}")

#  2.Handling Form Errors
def my_view(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # Process form data if valid
            return HttpResponse("Form submitted successfully!")
        else:
            # Return an error response if form is invalid
            return HttpResponse("Form submitted with invalid data")
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})

# Ensure that the DEBUG setting in settings.py is set to False when you want to display your custom 404 page in production.


# 3.Handling Permission Errors (PermissionDenied)
def my_view(request):
    # Check if the user has permission to view the object
    if not request.user.has_perm('myapp.view_mymodel'):
        raise PermissionDenied("You do not have permission to view this.")
    return HttpResponse("You have permission to view this content.")

# 4.Handling Multiple Object Exceptions (MultipleObjectsReturned)
def detail(request, id):
    try:
        # This assumes there should only be one product with this ID
        product = Product.objects.get(pk=id)
    except Product.MultipleObjectsReturned:
        # Handle case where multiple products are returned unexpectedly
        return HttpResponse("Multiple products found with this ID.")
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return HttpResponse(f"Product Found: {product.name}")


# 5.Handling Invalid Field Access (FieldDoesNotExist)
def access_field(request):
    try:
        field = Product._meta.get_field('non_existent_field')
    except FieldDoesNotExist:
        return HttpResponse("The field does not exist in the model.")
    return HttpResponse(f"Field value: {field}")

