from django.shortcuts import render, get_object_or_404
from .models import Warehouse
# Create your views here.

# show warehouse pages
# passing warehouse info
def warehouse_one(request, warehouse_id):
    warehouses = get_object_or_404(Warehouse, pk=warehouse_id)
    context = {'warehouse': warehouses}
    return render(request, 'warehouse/warehouse.html', context)
# Create your views here.

# show warehouse pages
# passing warehouse info
# def warehouse(request):
#    return render(request, 'warehouse/warehouse.html')

def warehouse(request):
    return render(request, 'warehouse/warehouses.html')
# show warehouse 
def show_region(request):
    pass


def order(request):
    pass