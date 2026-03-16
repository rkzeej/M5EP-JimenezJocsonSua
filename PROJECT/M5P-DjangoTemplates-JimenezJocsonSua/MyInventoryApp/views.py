from django.shortcuts import render
from .models import Supplier

# Create your views here.
def hello_world(request):
    return render(request, 'MyInventoryApp/hello_world.html')

def view_supplier(request):
        supplier_objects = Supplier.objects.all()
        return render(request, 'MyInventoryApp/view_supplier.html', {'suppliers':supplier_objects})