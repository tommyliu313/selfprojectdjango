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
    warehouse_item = Warehouse.objects.all()
    paginator = Paginator(warehouse_item, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'warehouse': paged_listings}
    return render(request, 'warehouse/warehouses.html', context)

# show warehouse 
def show_region(request, region_name):

    var_region = Warehouse.objects.filter(region=region_name)
    paginator = Paginator(var_region, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'region': paged_listings}
    return render(request,'warehouse/region.html', context)
    
#def show_region_slug(request,slugword):
#    variable = Warehouse.objects.get(slug=slugword)
#    context = {'warehouse': variable}
#    return render(request, 'warehouse/warehouse.html', context)

def process_order(request):
    if request.method == "POST":
        start_calendar = request.POST['startcalendar']
        end_calendar = request.POST['endcalendar']
        rentchoose = request.POST['rent_choose']
    else:
        pass
        
               