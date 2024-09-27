from django.shortcuts import render, get_object_or_404
from .models import Warehouse
from django.core.paginator import Paginator
# Create your views here.

# show warehouse pages
# passing warehouse info
def warehouse_one(request, warehouse_id):
    warehouses = get_object_or_404(Warehouse, pk=warehouse_id)
    context = {'warehouse': warehouses}
    return render(request, 'warehouse/warehouse.html', context)
# Create your views here.

def warehouse(request):
    var_region = Warehouse.objects.filter().order_by('region')
    paginator = Paginator(var_region, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'warehouse': var_region}
    return render(request, 'warehouse/warehouses.html', context)

# show warehouse 
def show_region(request, region):

    var_region = Warehouse.objects.filter().order_by('region')
    paginator = Paginator(var_region, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'region': var_region}
    return render(request,'warehouse/region.html', context)
    


def order(request):
    pass